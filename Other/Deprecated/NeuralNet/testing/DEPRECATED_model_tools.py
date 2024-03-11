import os
import pandas as pd
import tensorflow as tf
import ijson
import nltk
import numpy as np
import warnings
import gensim
import gensim.downloader as api
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
import tensorflow_hub as hub  # for using pre-trained embeddings directly within TF
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from PythonCode.NeuralNet.testing.DEPRECATED_model_test2 import TextClassificationModel

download_dir = os.getcwd()

nltk.download("punkt", download_dir=download_dir)
nltk.download("stopwords", download_dir=download_dir)
nltk.download("wordnet", download_dir=download_dir)
nltk.download("omw-1.4", download_dir=download_dir)

# file name for full arxiv dataset
# 'arxiv-metadata-oai-snapshot.json'

# file name for arxiv subset
# 'arxiv_metadata_formatted.json'
"""
DEFINITIONS:
- filename (str): path to your JSON data file
- batch_size (int): Number of samples per batch when training
- max_vocab_size (int): Limits the number of words in the tokenizer's vocabulary
- max_length (int): Length to which sequences will be padded/truncated
"""

"""
WHAT THIS IS SUPPOSED TO DO (HIGH LEVEL: IT IS NOT FULLY TESTED YET SO IT MAY CHANGE)
- Support for loading arXiv JSON data directly into a Pandas DataFrame
- Support for multiple preprocessing options (to make testing different ones easy)
    - TF's TextVectorization for tokenization and padding
    - TF's Hub KerasLayer for pre-trained word embeddings
    - NLTK for tokenization, lemmatization, and padding
    - gensim for pre-trained word embeddings
- Automatically splits dataset into training, validation, and testing sets
    - hopefully this will make it easy to evaluate the model
- Encodes categorical labels (the abstracts categories) using sklearn's MultiLabelBinarizer
    - This is for multi-label classification
- Creates TF datasets for processed features and labels
- Uses batching, shuffling, and prefeching to hopefully imporve model training performance

Example Usage:
1. Initialize ModelTools object with path to JSON. Optionally provide batch size, vocabulary size, and sequence length.
2. Call load_and_preprocess_data() to load and prepare the datasets.
3. Access the prepared TF datasets for training, validation, and testing via get_tf_dataset()
"""


class ModelTools:
    def __init__(
        self,
        filename: str,
        batch_size: int = 32,
        max_vocab_size: int = 11000,
        max_length: int = 500,
        use_word_embeddings: bool = True,
    ):

        USE_MODEL_URL = "https://tfhub.dev/google/universal-sentence-encoder/4"

        self.train_datset = None
        self.val_dataset = None
        self.test_dataset = None

        self.filename = filename
        self.batch_size = batch_size
        self.max_vocab_size = max_vocab_size
        self.max_length = max_length
        self.use_word_embeddings = use_word_embeddings
        self.mlb = MultiLabelBinarizer()
        self.tokenizer = Tokenizer(num_words=max_vocab_size, oov_token="<OOV>")

        # self.model_path = api.load("word2vec-google-news-300", return_path=True)
        self.embeddings_layer = None
        if use_word_embeddings:
            self.embeddings_layer = hub.KerasLayer(
                USE_MODEL_URL, input_shape=[], dtype=tf.string, trainable=True
            )

        self.text_vectorization = TextVectorization(
            max_tokens=max_vocab_size, output_sequence_length=max_length
        )

        self.df = pd.DataFrame()  # pandas dataframe to hold all data
        self.tf_dataset = None  # TensorFlow dataset
        if use_word_embeddings:
            self.word_vectors = api.load("word2vec-google-news-300")
        self.lemmatizer = WordNetLemmatizer()

    # call this first to process the file you initialized your object with
    def load_and_preprocess_data(self) -> None:
        try:
            with open(self.filename, "rb") as file:
                self.df = pd.DataFrame(list(ijson.items(file, "item")))
            if not {"abstract", "categories"}.issubset(self.df.columns):
                raise ValueError(
                    "Loaded data does not contain all the expected columns."
                )
        except FileNotFoundError as e:
            warnings.warn(f"File not found: {self.filename}")
            return
        except IOError as e:
            warnings.warn(f"IO error occured while loading {self.filename}: {e}")
            return
        except Exception as e:
            warnings.warn(f"Failed to load data from {self.filename}: {e}")
            return

        # Split the data first to avoid information leakage during vectorization fitting
        train_df, test_df = train_test_split(self.df, test_size=0.2, random_state=42)
        train_df, val_df = train_test_split(
            train_df, test_size=0.25, random_state=42
        )  # 0.25 x 0.8 = 0.2

        # if not self.use_word_embeddings:
        #     # Prepare text Vectorization layer
        #     # self.text_vectorization.adapt(train_df['abstract'].to_numpy())
        #     # train_texts = self.text_vectorization(train_df['abstract'].to_numpy())
        #     # val_texts = self.text_vectorization(val_df['abstract'].to_numpy())
        #     # test_texts = self.text_vectorization(test_df['abstract'].to_numpy())
        #     train_embeddings = self.embeddings_layer(train_df['abstract'])
        #     val_embeddings = self.embeddings_layer(val_df['abstract'])
        #     test_embeddings = self.embeddings_layer(test_df['abstract'])
        # else:
        #     # Directly use embeddings for TF models
        #     train_texts = train_df['abstract']
        #     val_texts = val_df['abstract']
        #     test_texts = test_df['abstract']
        #     train_embeddings = self.embeddings_layer(train_df['abstract'])
        #     val_embeddings = self.embeddings_layer(val_df['abstract'])
        #     test_embeddings = self.embeddings_layer(test_df['abstract'])

        # # Encode labels (categories)
        # self.mlb.fit(self.df['categories'].str.split(' ').tolist())
        # train_labels = self.mlb.transform(train_df['categories'].str.split(' ').tolist())
        # val_labels = self.mlb.transform(val_df['categories'].str.split(' ').tolist())
        # test_labels = self.mlb.transform(test_df['categories'].str.split(' ').tolist())

        # # # Create TF dataset
        # # self.train_dataset = tf.data.Dataset.from_tensor_slices((train_texts, train_labels)).shuffle(len(train_texts)).batch(self.batch_size).prefetch(tf.data.AUTOTUNE)
        # # self.val_dataset = tf.data.Dataset.from_tensor_slices((val_texts, val_labels)).batch(self.batch_size).prefetch(tf.data.AUTOTUNE)
        # # self.test_dataset = tf.data.Dataset.from_tensor_slices((test_texts, test_labels)).batch(self.batch_size).prefetch(tf.data.AUTOTUNE)

        # self.train_dataset = tf.data.Dataset.from_tensor_slices((train_embeddings, train_labels))
        # self.val_dataset = tf.data.Dataset.from_tensor_slices((val_embeddings, val_labels))
        # self.test_dataset = tf.data.Dataset.from_tensor_slices((test_embeddings, test_labels))

        # # Apply batching, shuffling, and prefetching to optimize training
        # self.train_dataset = self.train_dataset.shuffle(buffer_size=len(train_embeddings)).batch(self.batch_size).prefetch(tf.data.AUTOTUNE)
        # self.val_dataset = self.val_dataset.batch(self.batch_size).prefetch(tf.data.AUTOTUNE)
        # self.test_dataset = self.test_dataset.batch(self.batch_size).prefetch(tf.data.AUTOTUNE)

        # self.inspect_dataset(self.train_dataset)
        # # CHANGES EXPLAINED
        # # preprocessing and vectorization methods are unecessary if using TextVectorization or hub.KerasLayer for embeddings
        # # This is why they have been removed from the class and moved to the bottom of the file and commented out

        train_texts = train_df["abstract"].values
        val_texts = val_df["abstract"].values
        test_texts = test_df["abstract"].values

        # Encode labels (categories)
        self.mlb.fit(self.df["categories"].str.split(" ").tolist())
        train_labels = self.mlb.transform(
            train_df["categories"].str.split(" ").tolist()
        )
        val_labels = self.mlb.transform(val_df["categories"].str.split(" ").tolist())
        test_labels = self.mlb.transform(test_df["categories"].str.split(" ").tolist())

        # Create TF dataset
        self.train_dataset = (
            tf.data.Dataset.from_tensor_slices((train_texts, train_labels))
            .shuffle(len(train_texts))
            .batch(self.batch_size)
            .prefetch(tf.data.AUTOTUNE)
        )
        self.val_dataset = (
            tf.data.Dataset.from_tensor_slices((val_texts, val_labels))
            .batch(self.batch_size)
            .prefetch(tf.data.AUTOTUNE)
        )
        self.test_dataset = (
            tf.data.Dataset.from_tensor_slices((test_texts, test_labels))
            .batch(self.batch_size)
            .prefetch(tf.data.AUTOTUNE)
        )

        # Apply batching, shuffling, and prefetching to optimize training
        self.train_dataset = (
            self.train_dataset.shuffle(buffer_size=len(train_texts))
            .batch(self.batch_size)
            .prefetch(tf.data.AUTOTUNE)
        )
        self.val_dataset = self.val_dataset.batch(self.batch_size).prefetch(
            tf.data.AUTOTUNE
        )
        self.test_dataset = self.test_dataset.batch(self.batch_size).prefetch(
            tf.data.AUTOTUNE
        )

        self.inspect_dataset(self.train_dataset)

    def inspect_dataset(self, dataset):
        # inspecting the first batch of the given dataset
        for text_batch, label_batch in dataset.take(1):
            print("TEXT BATCH SHAPE: ", text_batch.shape)
            print("LABEL BATCH SHAPE: ", label_batch.shape)
            print(text_batch.numpy()[:3])  # display embedding for first 3 samples
            print(label_batch.numpy()[:3])  # display labels for first 3 samples

    def get_tf_dataset(self):
        return self.train_dataset, self.val_dataset, self.test_dataset


if __name__ == "__main__":
    filename = "arxiv_metadata_formatted.json"
    tools = ModelTools(filename=filename)
    tools.load_and_preprocess_data()
    train_dataset, val_dataset, _ = tools.get_tf_dataset()

    num_classes = len(tools.mlb.classes_)
    text_model = TextClassificationModel(
        num_classes=num_classes,
        use_pretrained_embeddigns=True,
        max_features=11000,
        sequence_length=500,
    )
    text_model.compile_model()
    text_model.train_model(train_dataset, val_dataset, epochs=10)
    model = text_model.get_model()

"""
PREVIOUS FUNCTIONS BELOW

"""

# # call this first to process the file you initialized your object with
# def load_and_preprocess_data(self) -> None:
#     """Loads data from JSON file into a Pandas DataFrame and preprocesses text."""
#     try:
#         # Load data
#         with open(self.filename, 'rb') as file:
#             self.df = pd.DataFrame(list(ijson.items(file, 'item')))
#         # Validate that the dataframe has the expected columns
#         expected_columns = ['abstract', 'categories']
#         if not all(column in self.df.columns for column in expected_columns):
#             raise ValueError("Loaded data does not contain all the expected columns.")
#     except FileNotFoundError as e:
#         warnings.warn(f"File not found: {self.filename}")
#         return
#     except IOError as e:
#         warnings.warn(f"IO error occured while loading {self.filename}: {e}")
#         return
#     except Exception as e:
#         warnings.warn(f"Failed to load data from {self.filename}: {e}")
#         return

#     # Preprocess abstracts
#     self.df['processed_abstracts'] = self.df['abstract'].apply(self._preprocess_text)
#     if self.use_word_embeddings:
#         self.df['vectorized_abstracts'] = self.df['processed_abstracts'].apply(self._vectorize_text)
#     else:
#         # Tokenize and pad abstracts
#         self.df['tokenized_abstracts'] = self.tokenizer.texts_to_sequences(self.df['processed_abstracts'])
#         self.df['padded_abstracts'] = list(pad_sequences(self.df['tokenized_abstracts'],
#                                                         maxlen=self.max_length,
#                                                         padding='post',
#                                                         truncating='post'))

#     # Split categories and encode
#     self.df['categories_list'] = self.df['categories'].str.split(' ')
#     self.encoded_categories = self.mlb.fit_transform(self.df['categories_list'].tolist())

#     # Create TF dataset
#     self.make_tf_dataset()

# def _preprocess_text(self, text: str) -> str:
#     """Preprocess a single text abstract by removing stopwords and tokenizing."""
#     text = text.lower() # Make lowercase to ensure consistency
#     stop_words = set(stopwords.words('english'))
#     word_tokens = word_tokenize(text)
#     # Lemmatize (reduce words to their root form) if it's not a stopword
#     lemmatized_sequence = [self.lemmatizer.lemmatize(word) for word in word_tokens if word not in stop_words]
#     return " ".join(lemmatized_sequence)

# def _vectorize_text(self, text: str):
#     """Averages word vectors for a text abstract"""
#     vectors = [self.word_vectors[word] for word in text.split() if word in self.word_vectors]
#     if vectors:
#         return np.mean(vectors, axis=0)
#     else:
#         # Add small epsilon value to the zero vector to account for models that don't like zero vectors
#         epsilon = 1e-9
#         return np.zeros(300) + epsilon

# def get_tf_dataset(self) -> tf.data.Dataset:
# """Returns the TF dataset created by make_tf_dataset()"""
# if self.tf_dataset is not None:
#     return self.tf_dataset
# else:
#     print("No TF dataset to return. Ensure dataset has been made.")
#     return None

# def make_tf_dataset(self) -> None:
#     """Converts preprocessed data and encoded labels into a TF dataset"""
#     features = None
#     if self.use_word_embeddings:
#         features = np.stack(self.df['vectorized_abstracts'].values)
#     else:
#         self.df['tokenized_abstracts'] = self.tokenizer.texts_to_sequences(self.df['processed_abstracts'])
#         self.df['padded_abstracts'] = list(pad_sequences(self.df['tokenized_abstracts'],
#                                                          maxlen=self.max_length,
#                                                          padding='post',
#                                                          truncating='post'))
#         features = np.array(self.df['padded_abstracts'].tolist())

#     if not self.df.empty and self.encoded_categories is not None:
#         self.tf_dataset = tf.data.Dataset.from_tensor_slices((features, self.encoded_categories))
#         self.tf_dataset = self.tf_dataset.shuffle(buffer_size=len(self.df))
#         self.tf_dataset = self.tf_dataset.batch(self.batch_size)
#         self.tf_dataset = self.tf_dataset.prefetch(buffer_size=tf.data.AUTOTUNE)
#     else:
#         warnings.warn("DataFrame is empty or categories are not encoded. Ensure data is loaded and preprocessed")
