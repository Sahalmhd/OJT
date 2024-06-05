# join the two array
import numpy as np 
array1 = np.array([1,2,3,])
array2 = np.array([4,5,6])

concat_array = np.concatenate((array1,array2))
print ("concat_array :",concat_array)

#create a multi dementianal array
array2D_1 = np.array([[1,2,3],[4,5,6]])
array2D_2 = np.array([[7,8,9],[10,11,12]])

# verticaly and horizontaly join
# vstack - is the methord used to join verticaly
# hstack - is the methord used to join horizondaly

# verticaly join 
#vstack_array = np.vstack((array2D_1,array2D_2))
#print ("vertical stacked is:", vstack_array)

# horizontaly join
hsrack_array = np.hstack((array2D_1,array2D_2))
print("hirizontal stacked is:", hsrack_array)