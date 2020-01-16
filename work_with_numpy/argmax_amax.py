# https://www.geeksforgeeks.org/numpy-argmax-python/
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.amax.html

# Python Program illustarting 
# working of argmax() 

import numpy as np 

# Working on 2D array 
array = np.random.randint(16, size=(4, 4)) 
print("INPUT ARRAY : \n", array) 

# No axis mentioned, so works on entire array 
print("\nIndice of Max element : ", np.argmax(array)) 
print("\nMax element : ", array.flatten('C')[np.argmax(array)]) 
print("\nMax element : ", np.amax(array))

# returning Indices of the max element 
# as per the indices 

print("\nIndices of Max element : ", np.argmax(array, axis = 0)) 
print("\nMax element : ", np.amax(array, axis = 0))
print("\nIndices of Max element : ", np.argmax(array, axis = 1)) 
print("\nMax element : ", np.amax(array, axis = 1))
