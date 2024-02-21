import pandas as pd
import tensorflow as tf
import ijson
import nltk
from sklearn.preprocessing import MultiLabelBinarizer
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

# file name
# 'arxiv-metadata-oai-snapshot.json'

class ModelTools:
    def __init__(self, filename: str, batch_size: int = 32, 
                 max_vocab_size: int = 25000, 
                 max_length: int = 200):
        self.filename = filename
        self.batch_size = batch_size
        self.max_vocab_size = max_vocab_size
        self.max_length = max_length
        self.raw_abstracts = []       
        self.formatted_abstracts = [] # Data
        self.categories = [] # Labels
        self.mlb = MultiLabelBinarizer() # Multi-Label Binarizer Object
        self.encoded_categories = None
        self.tf_dataset = None
        self.tokenizer = Tokenizer(num_words=max_vocab_size, oov_token="<OOV>")
        
    # call this first to process the file you initialized your object with
    def preprocess_data(self) -> None:
        """
        Reads and preprocesses data from JSON file.
        
        Includes tokenization and removal of stopwords from abstracts 
        """
        try:
            with open(self.filename, 'rb') as file:
                for item in ijson.items(file, 'item'):
                    self.raw_abstracts.append(item['abstract'])
                    self.categories.append(item['categories'].split(' '))
            # Preprocess abstracts
            self.formatted_abstracts = self._preprocess_abstracts(self.raw_abstracts)
        except Exception as e:
            print(f"Error processing data: {e}")
            # Handle or raise exception, right now we just print it
            # and continue
            
    # call this second to encode your labels
    def encode_labels(self) -> None:
        """
        Encodes the category labels into a binary format suitable for multi-label classification.
        """
        if self.categories:
            self.encoded_categories = self.mlb.fit_transform(self.categories)
        else:
            print("No categories to encode. Ensure preprocess_data() has been called first.")

    # Call this third to convert data to a TF dataset
    def make_tf_dataset(self) -> None:
        """
        Converts preprocessed data and encoded labels into a TF dataset.
        """
        if self.formatted_abstracts and self.encoded_categories is not None:
            dataset = tf.data.Dataset.from_tensor_slices((self.formatted_abstracts, self.encoded_categories))
            dataset = dataset.shuffle(buffer_size=len(self.formatted_abstracts))
            dataset = dataset.batch(self.batch_size)
            dataset = dataset.prefetch(buffer_size=tf.data.AUTOTUNE)
            self.tf_dataset = dataset
        else:
            print("Data not ready for dataset creation. Ensure preprocess_data() and encode_labels() have been called first")

    # call this to get your TF dataset that make_tf_dataset() creates
    def get_tf_dataset(self) -> tf.data.Dataset:
        if self.tf_dataset is not None:
            return self.tf_dataset
        else:
            print("No TF dataset to return. Ensure make_tf_dataset() has been called first.")
            return None

    # private class method, do NOT call
    def _preprocess_abstracts(self, abstracts):
        """
        Internal class method to preprocess abstracts via removing stopwords and tokenization
        """
        stop_words = set(stopwords.words('english'))
        
        # temp abstracts list to avoid potential errors with the class formatted_abstracts list
        preprocessed_abstracts = []
        
        for abstract in abstracts:
            word_tokens = word_tokenize(abstract)
            filtered_sentence = [word for word in word_tokens if not word.lower() in stop_words]
            preprocessed_abstracts.append(" ".join(filtered_sentence))
        
        # Tokenize and pad abstracts
        self.tokenizer.fit_on_texts(preprocessed_abstracts)
        sequences = self.tokenizer.texts_to_sequences(preprocessed_abstracts)
        padded_sequences = pad_sequences(sequences, maxlen=self.max_length, padding='post', truncating='post')
        return padded_sequences