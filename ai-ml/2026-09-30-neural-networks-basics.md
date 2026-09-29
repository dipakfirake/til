# Neural Networks Basics

> _2026-09-30_ | Category: **ai-ml**

How machines learn.

An Artificial Neural Network (ANN) consists of:
1. **Input Layer**: Takes features (e.g., image pixels).
2. **Hidden Layers**: Perform computations using Weights and Biases.
3. **Output Layer**: Produces prediction (e.g., cat vs dog).

**Forward Propagation**: Data moves input -> output.
`Z = W*X + b`
`A = Activation(Z)`

**Backpropagation**: Calculates error (Loss) and updates weights backwards using Gradient Descent to minimize the error.

**Key Takeaway**: Training a model is just finding the optimal weights and biases that minimize the loss function across the dataset.
