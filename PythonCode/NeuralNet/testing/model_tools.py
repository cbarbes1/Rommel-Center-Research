import os
import pandas as pd
import tensorflow as tf
import ijson
import nltk
import numpy as np
import warnings
import gensim.downloader as api
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization

from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

download_dir = os.getcwd()

nltk.download('punkt', download_dir=download_dir)
nltk.download('stopwords', download_dir=download_dir)
nltk.download('wordnet', download_dir=download_dir)
nltk.download('omw-1.4', download_dir=download_dir)
# file name
# 'arxiv-metadata-oai-snapshot.json'

"""
DEFINITIONS:
- filename (str): path to your JSON data file
- batch_size (int): Number of samples per batch when training
- max_vocab_size (int): Limits the number of words in the tokenizer's vocabulary
- max_length (int): Length to which sequences will be padded/truncated
"""

"""
EXAMPLE USAGE:

# INTIALIZATION

tools = ModelTools(filename='arxiv-metadata-oai-snapshot.json', batch_size=32, max_vocab_size=25000, max_length=200)

tools.load_and_preprocess_data()

# LOADING/ PREPROCESSING OF DATA

Calling tools.load_and_preprocess_data() starts data loading and preprocessing workflow

How it works (theoretically):
- JSON file is read into a Pandas Dataframe (self.df). Each row corresponds to an entry in the JSON file, with columns for each attribute ('id', 'abstract', 'categories', etc)

**Preprocessing abstracts:**
- Text Cleaning and Tokenization: Each abstract is processed by '_preprocess_text()', which removes stopwords and tokenizes the text (splits it into words or tokens)

Example transformation:
The Abstract: 
"Quantum computing offers promising solutions. However, challenges remain."

Becomes:
"Quatum computing offers promising solutions However challenges remain"

self.df['processed_abstracts'] is created by applying _preprocess_text() to each abstract



**Tokenize and Pad abstracts**
How it works (theoretically):
- Abstracts are converted into sequences of ints using the tf Tokenizer, each integer represents a unique word.
- Sequences are then padded to ensure they all have the same length of 'max_length'

Example transformation:
Categories:
"quant-ph cs.LG"

Become:
A binary representation, something like [1, 0, 1, 0, ...]
The above matrix is stored in 'self.encoded_categories'



# CREATING TF DATASET
TF dataset 'self.tf_dataset' begins and None and is created from the padded abstract sequences and the binary encoded categories

'tf.data.Dataset.from_tensor_slices()' pairs each abstract with its corresponding category vector. The dataset is then shuffled and batched according to 'self.batch_size'
it is then prefetcehd to (hopefully) optimize training performance



# ACCESSING TF DATASET
'tools.get_tf_dataset()' can be called, it will return the TF dataset ready to use in training of a model
Note: if the TF dataset has not yet been created it will inform the user they need to go through those steps first.
"""

class ModelTools:
    def __init__(self, filename: str, batch_size: int = 32, 
                 max_vocab_size: int = 25000, max_length: int = 200, 
                 use_word_embeddings: bool = False):
        self.filename = filename
        self.batch_size = batch_size
        self.max_vocab_size = max_vocab_size
        self.max_length = max_length
        self.use_word_embeddings = use_word_embeddings
        self.mlb = MultiLabelBinarizer()
        self.tokenizer = Tokenizer(num_words=max_vocab_size, oov_token="<OOV>")
        self.df = pd.DataFrame() # pandas dataframe to hold all data
        self.tf_dataset = None # TensorFlow dataset
        if use_word_embeddings:
            self.word_vectors = api.load("word2vec-google-news-300")
        self.lemmatizer = WordNetLemmatizer()
        
    # call this first to process the file you initialized your object with
    def load_and_preprocess_data(self) -> None:
        """Loads data from JSON file into a Pandas DataFrame and preprocesses text."""
        try:
            # Load data
            with open(self.filename, 'rb') as file:
                self.df = pd.DataFrame(list(ijson.items(file, 'item')))
            # Validate that the dataframe has the expected columns
            expected_columns = ['abstract', 'categories']
            if not all(column in self.df.columns for column in expected_columns):
                raise ValueError("Loaded data does not contain all the expected columns.")
        except FileNotFoundError as e:
            warnings.warn(f"File not found: {self.filename}")
            return
        except IOError as e:
            warnings.warn(f"IO error occured while loading {self.filename}: {e}")
            return
        except Exception as e:
            warnings.warn(f"Failed to load data from {self.filename}: {e}")
            return
        
        # Preprocess abstracts
        self.df['processed_abstracts'] = self.df['abstract'].apply(self._preprocess_text)
        if self.use_word_embeddings:
            self.df['vectorized_abstracts'] = self.df['processed_abstracts'].apply(self._vectorize_text)
        else:
            # Tokenize and pad abstracts
            self.df['tokenized_abstracts'] = self.tokenizer.texts_to_sequences(self.df['processed_abstracts'])
            self.df['padded_abstracts'] = list(pad_sequences(self.df['tokenized_abstracts'], 
                                                            maxlen=self.max_length, 
                                                            padding='post', 
                                                            truncating='post'))
        
        # Split categories and encode
        self.df['categories_list'] = self.df['categories'].str.split(' ')
        self.encoded_categories = self.mlb.fit_transform(self.df['categories_list'].tolist())
        
        # Create TF dataset
        self.make_tf_dataset()
        
    def _preprocess_text(self, text: str) -> str:
        """Preprocess a single text abstract by removing stopwords and tokenizing."""
        text = text.lower() # Make lowercase to ensure consistency
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(text)
        # Lemmatize (reduce words to their root form) if it's not a stopword
        lemmatized_sequence = [self.lemmatizer.lemmatize(word) for word in word_tokens if word not in stop_words]
        return " ".join(lemmatized_sequence)

    def _vectorize_text(self, text: str):
        """Averages word vectors for a text abstract"""
        vectors = [self.word_vectors[word] for word in text.split() if word in self.word_vectors]
        if vectors:
            return np.mean(vectors, axis=0)
        else:
            # Add small epsilon value to the zero vector to account for models that don't like zero vectors
            epsilon = 1e-9
            return np.zeros(300) + epsilon
        
    def make_tf_dataset(self) -> None:
        """Converts preprocessed data and encoded labels into a TF dataset"""
        features = None
        if self.use_word_embeddings:
            features = np.stack(self.df['vectorized_abstracts'].values)
        else:
            self.df['tokenized_abstracts'] = self.tokenizer.texts_to_sequences(self.df['processed_abstracts'])
            self.df['padded_abstracts'] = list(pad_sequences(self.df['tokenized_abstracts'],
                                                             maxlen=self.max_length,
                                                             padding='post',
                                                             truncating='post'))
            features = np.array(self.df['padded_abstracts'].tolist())
            
        if not self.df.empty and self.encoded_categories is not None:
            self.tf_dataset = tf.data.Dataset.from_tensor_slices((features, self.encoded_categories))
            self.tf_dataset = self.tf_dataset.shuffle(buffer_size=len(self.df))
            self.tf_dataset = self.tf_dataset.batch(self.batch_size)
            self.tf_dataset = self.tf_dataset.prefetch(buffer_size=tf.data.AUTOTUNE)
        else:
            warnings.warn("DataFrame is empty or categories are not encoded. Ensure data is loaded and preprocessed")
            
    def get_tf_dataset(self) -> tf.data.Dataset:
        """Returns the TF dataset created by make_tf_dataset()"""
        if self.tf_dataset is not None:
            return self.tf_dataset
        else:
            print("No TF dataset to return. Ensure dataset has been made.")
            return None