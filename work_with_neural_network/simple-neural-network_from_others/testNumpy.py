import numpy as np

# sigmoid function to normalize inputs
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# sigmoid derivatives to adjust synaptic weights
def sigmoid_derivative(x):
    return x * (1 - x)

# input dataset
training_inputs = np.array([[0,0,1],
                            [1,1,1],
                            [1,0,1],
                            [0,1,1]])

# output dataset
training_outputs = np.array([[0,1,1,0]]).T
print('Training_outputs: ')
print(training_outputs)
training_outputs_noT = np.array([[0,1,1,0]])
print('Training_outputs without T: ')
print(training_outputs_noT)

# seed random numbers to make calculation
np.random.seed(1)

# initialize weights randomly with mean 0 to create weight matrix, synaptic weights
synaptic_weights = 2 * np.random.random((3,4,2,5)) - 1

print('Random starting synaptic weights: ')
print(synaptic_weights)
