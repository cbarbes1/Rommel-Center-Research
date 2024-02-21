import pandas as pd
import tensorflow as tf
import ijson
import nltk
import warnings
import gensim.downloader as api
from sklearn.preprocessing import MultiLabelBinarizer
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

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
        
    # call this first to process the file you initialized your object with
    def load_and_preprocess_data(self) -> None:
        """Loads data from JSON file into a Pandas DataFrame and preprocesses text."""
        try:
            # Load data
            with open(self.filename, 'rb') as file:
                data = list(ijson.items(file, 'item'))
                self.df = pd.DataFrame(data)
        except Exception as e:
            warnings.warn(f"Failed to load data from {self.filename}: {e}")
            return
        
        # Preprocess abstracts
        self.df['processed_abstracts'] = self.df['abstract'].apply(self._preprocess_text)
        
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
        filtered_sentence = [word for word in word_tokens if not word.lower() in stop_words]
        return " ".join(filtered_sentence)

    def make_tf_dataset(self) -> None:
        """Converts preprocessed data and encoded labels into a TF dataset"""
        if not self.df.empty and self.encoded_categories is not None:
            dataset = tf.data.Dataset.from_tensor_slices((self.df['padded_abstracts'].tolist(), 
                                                          self.encoded_categories))
            self.tf_dataset = dataset.shuffle(buffer_size=len(self.df))
            self.tf_dataset = self.tf_dataset.batch(self.batch_size)
            self.tf_dataset = self.tf_dataset.prefetch(buffer_size=tf.data.AUTOTUNE)
        else:
            warnings.warn("Dataframe is empty or categories are not encoded. Ensure data is loaded and preprocessed")
            
    def get_tf_dataset(self) -> tf.data.Dataset:
        """Returns the TF dataset created by make_tf_dataset()"""
        if self.tf_dataset is not None:
            return self.tf_dataset
        else:
            print("No TF dataset to return. Ensure dataset has been made.")
            return None