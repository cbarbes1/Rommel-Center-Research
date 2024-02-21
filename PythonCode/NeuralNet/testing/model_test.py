from pullArxivCatsFromJson import GetArxivCatsFromJson
import tensorflow as tf
from sklearn.preprocessing import MultiLabelBinarizer
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, GlobalAveragePooling1D, Dense, Dropout
from tensorflow.keras.metrics import BinaryAccuracy

"""
When we have abstracts with their associated categories first step is to encode
the caategories for multi-lable classification. We can use the MultiLabelBinarizer
from sklearn.preprocessing to do this.

arxiv_ab_cats is a dictionary where a key is the abstract and the value is a list of categories

the preceding loop goes through and adds each key:value pair into the same index of the two lists.

So the first abstract:value pair will both be at index 0 in their corresponding abstracts and categories lists
"""

# For preparing dataset
#from sklearn.preprocessing import MultiLabelBinarizer

arxiv_ab_cats: dict = GetArxivCatsFromJson().get_arxiv_ab_cat_dict()
#print(arxiv_ab_cats)

abstracts = []
categories = []

for abstract, category in arxiv_ab_cats.items():
    abstracts.append(abstract)
    categories.append(category)

#print(abstracts)
#print("\n\n\n")
#print(categories)
# MultiLabelBinarizer object
mlb = MultiLabelBinarizer()

encoded_cats = mlb.fit_transform(categories)
print(encoded_cats)



"""
Text Processing

In this step we should process the abstracts in order to convert them into a numerical format that can
be fed into the neural network

This involves tokenization and padding
"""

# For text processing
#from tensorflow.keras.preprocessing.text import Tokenizer
#from tensorflow.keras.preprocessing.sequence import pad_sequences
#print(tf.__version__)

tokenizer = Tokenizer(num_words=10115, oov_token="<OOV>")
tokenizer.fit_on_texts(abstracts)
sequences = tokenizer.texts_to_sequences(abstracts)
padded_sequences = pad_sequences(sequences, maxlen=1000, padding='post')



# Defining the Model
#from tensorflow.keras.models import Sequential
#from tensorflow.keras.layers import Embedding, GlobalAveragePooling1D, Dense

model = Sequential([
    Embedding(input_dim=10115, output_dim=16, input_length=1000),
    Dropout(0.2),
    GlobalAveragePooling1D(),
    Dense(128, activation='relu'),
    Dropout(0.2),
    Dense(len(mlb.classes_), activation='sigmoid')
])

"""
Versions of each metric to see which works better
"""

# with the BinaryAccuracy metric
#model.compile(optimizer='adam', loss='binary_crossentropy', metrics=[BinaryAccuracy(name='accuracy')])

# allow tensorflow to determine the best metric
#model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Precision
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=[tf.keras.metrics.Precision(name='precision')])

# Recall
#model.compile(optimizer='adam', loss='binary_crossentropy', metrics=[tf.keras.metrics.Recall(name='recall')])

# F1 Score
#encoded_cats_for_F1 = mlb.fit_transform(categories)
#encoded_cats_for_F1 = tf.cast(encoded_cats_for_F1, tf.float32)
#model.compile(optimizer='adam', loss='binary_crossentropy', metrics=[tf.keras.metrics.F1Score(average='micro')])

"""
Training the Model

feed padded sequences of abstracts and the binary-encoded categories
"""
# Training the model
model.fit(padded_sequences, encoded_cats, epochs=10, validation_split=0.2)

# fit for F1
#model.fit(padded_sequences, encoded_cats_for_F1, epochs=10, validation_split=0.3)
