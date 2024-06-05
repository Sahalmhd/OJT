# converting iD into 2D
# .reshape() is the methord which is used for reshape the arrays.

import numpy as np

#create a 1D array
array_1D = np.array([1,2,3,4,5,6])
print("array1D :", array_1D)
print("shape of  array1D :", array_1D.shape)

#reshape the 1D array to array
array_2D = array_1D.reshape(2,3)
print ("2D array :", array_2D)
print("shape of array_2D :", array_2D.shape)

#reshape 1D array in to 3D array
array_3D = array_1D.reshape(2,3,1)
print("3D array :", array_3D)
print ("shape of array_3D :", array_3D.shape)

# resahpe BACK A 2D ARRAY TO 1D ARRAY
array_1D_back = array_2D.reshape(1,6)
print ("array_1D_back :", array_1D_back)
print ("shape of the array_1D_back :", array_1D_back.shape)