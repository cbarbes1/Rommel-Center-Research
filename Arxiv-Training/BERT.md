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
## Best Practices
