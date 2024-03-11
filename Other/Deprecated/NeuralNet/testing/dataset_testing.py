import tensorflow_datasets as tfds

# Load hugginface arxiv data set:
# https://huggingface.co/datasets/arxiv_dataset
# https://www.tensorflow.org/datasets/community_catalog/huggingface/arxiv_dataset
ds = tfds.load("huggingface:arxiv_dataset")

# Convert first batch to numpy and print
for example in ds.take(1).as_numpy_iterator():
    print(example)
