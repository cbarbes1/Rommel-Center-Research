# NLP
Enables computers to understand language like humans do 
lay the foundation for all ai chatbots

First data gets preprocessed

Common analysis methods
- based or ML
- Syntax or semantic analysis
- syntax - analyzed based on grammar 
- Identify root of the work
- semantic- how words are used
- Grouping words
- many implementations

challenges:
languages always evolving

# BERT 
## What is bert?
- NLP model
- Designed to understand the meaning of ambiguous language in text by using surrounding text to find context
- Pretrained using wikipedia and can be fine-tuned with qand a data sets
- Bidirectional Encoder Representations from transformers
- Based on deep learning model where output is connected to input
- Weights between them is based upon their connection

## History
In 2017 google introduced transformer model
At this point LMs used recurrent neural networks (RNN) and convolutional neural networks (CNN) to hangle NLP tasks
CNNs and RNNs are competent models however they require sequences of data to be processed in a fixed order. 
Transformer models are considered a significant improvement because they dont require data sequences to be processed in any fixed order
This enabled training on larger data, facilitating models like BERT

## How BERT Works
Leveraging the transformers
transformers process any given word in relation to all other words in a sentence, rather than one at a time
This process enables to extract the full context of the word
Masked Language Modeling is used 
# BERTopic
## Serialization
Generally advised to use .safetensors to save the bert model
other forms, .pickle and .bin are also valid
### Saving
Three methods: 
- .safetensors and .bin can save a light model with config files
- .pickle can save full model

- Using safe tensors
```py
embedding_model = "sentence-transformers/all-MiniLM-L6-v2"
topic_model.save("path/to/my/model_dir", serialization="safetensors", save_ctfidf=True, save_embedding_model=embedding_model)
```
## BERTopic layout
- Embed the text
- Dimensionality Reduction - using UMAP
- Cluster Documents - HDBSCAN
- Bag-of-Words - 
- Topic Representation
     - TF-IDF is modified to help get the topics
     - Class based TF-IDF

