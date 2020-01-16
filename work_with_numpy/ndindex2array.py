import numpy as np

shape = (2,3)
index = np.ndindex(shape)
states = np.reshape(np.array(list(np.ndindex(shape)), 'int, int'), shape)
print(list(np.ndindex(shape)))
print(states)
print(states[0, 2])
