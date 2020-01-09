# https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-8.php

import numpy as np
x = np.ones((5,5))
print("Original array:")
print(x)
print("1 on the border and 0 inside in the array")
x[1:-1,1:-1] = 0
print(x)


print("one dimension array to show index")
y = np.array(range(5))
print(y)
print(y[:-1])
