# Design Document for RNN Architecture

## Model Architecture Components

- **Input Layer**: 
  - Accepts sequences of a batch of abstracts.
  
- **Embedding Layer**: 
  - 300-dimensional GloVe vectors for word representation.
  
- **Bidirectional LSTM Layers**: 
  - Features two layers, each with 128 LSTM units (Neurons), for bidirectional text processing.
  - Includes L2 regularization to mitigate potential overfitting.
  
- **Attention Layer**: 
  - 8-head attention to identify key parts of abstracts.
  
- **Batch Normalization Layer**: 
  - Applies normalization to stabilize and accelerate training.
  
- **Dense Layer**: 
  - ReLU activation
  - Fully connected to the attention layer's output.
  
- **Output Layer**: 
  - Uses softmax to create a probability distribution over categories.

## Training Guidelines

- **Dropout**: 
  - Dropout rate of 20% is to be used in otder to prevent overfitting.
  
- **Dataset**: 
  - The training set consists of 2 million categorized abstracts from Web of Science.
  
- **Optimizer**: 
  - Adam
  - Chosen for adaptive learning rate optimization.
  
- **Activation Functions**: 
  - ReLU
  - Chosen for non-linear processing in dense layers.
  
- **Loss Function**: 
  - Categorical cross-entropy used to evaluate predictions.

- **Learning Rate**: 
  - Starts at 0.001, with adjustments from a learning rate scheduler.

## Justification for RNN Architecture Over Transformers

When usung smaller datasets or limited in computational power RNNs can be more effective.
- See: https://arxiv.org/pdf/2009.05451.pdf

## Glossary of Terms

- **GloVe Vectors**: Pre-trained vectors that encode words into a dense space based on their co-occurrence in a large corpus, capturing semantic similarities.
- **Bidirectional LSTM (Long Short-Term Memory)**: A type of recurrent neural network capable of learning long-term dependencies. Processing text in both directions ensures that the context from both the past and the future is used for prediction at any point.
- **L2 Regularization**: A regularization technique that discourages learning a more complex or flexible model to prevent overfitting by adding a penalty on the magnitude of coefficients.
- **Attention Mechanism**: Allows the model to weigh the importance of different words in the text, focusing on the most informative parts to make decisions.
- **Batch Normalization**: A technique to normalize the inputs of each layer, so as to keep the activation values from becoming too high or too low, which can speed up training and improve the overall performance of the model.
- **Dense Layer**: A fully connected neural network layer where each input node is connected to each output node. The dense layer applies a linear operation on the input with the set of learned weights, which is followed by an activation function like ReLU.
- **ReLU (Rectified Linear Unit)**: An activation function that outputs the input directly if it is positive, otherwise, it will output zero. It is used to introduce non-linearity into the network, allowing it to learn more complex functions.
- **Softmax Function**: A function that turns logits, the raw output of the last layer of a neural network, into probabilities by taking the exponentials of each output and then normalizing these values by dividing by the sum of all the exponentials.
- **Dropout**: A regularization technique where randomly selected neurons are ignored during training, reducing the sensitivity to the specific weights of individual neurons.
- **Optimizer**: An algorithm or method used to change the attributes of the neural network such as weights and learning rate to reduce the losses. Adam optimizer is commonly used because it combines the best properties of the AdaGrad and RMSProp algorithms to provide an optimization algorithm that can handle sparse gradients on noisy problems.
- **Categorical Cross-Entropy**: A loss function that measures the dissimilarity between the distribution of the observed class labels and the predicted probabilities of class membership. Ideal for multi-class classification problems where each example belongs to one of L classes.
- **Learning Rate**: The magnitude of the steps taken during the optimization process to minimize the loss function. A crucial parameter that can determine the effectiveness and speed of training a neural network model.
