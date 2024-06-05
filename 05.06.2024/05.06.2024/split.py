import numpy as np
# split will works in numpy

array = np.array([1,2,3,4,5,6,7,8,9])
split_array = np.split(array,3)
print('oraginal array:', array)
print ('split_array:', split_array)


# multi dimational array
# horizontaly and verticaly

array_2D = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
vsplit_array = np.vsplit(array_2D,2)
print ('vsplited array :', vsplit_array)

# horizontaly split
hsplit_array = np.hsplit(array_2D,3)
print ('hsplited array ;', hsplit_array)