import numpy as np

shape = (6, 9)
states = np.ndindex(shape)

# [print(s) for s in states]

# print("Another line\n")
# [print(s) for s in states]

ar = np.zeros(shape, dtype=int)
ar[0,0] = 1
ar[1,-1] = 1
print(ar)
print(ar.shape)
print(list(states))


