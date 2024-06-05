import numpy as np

# for - in loop
# Id array
array_1D = np.array([1,2,3,4,5,6])
# iterate the elements in this array
print("array_1D :", array_1D)
for element in array_1D:
    print(element)

array_2D = np.array([[1,2,3,],[4,5,6],[7,8,9]])
print('2D array:', array_2D)
#ithratre 2 D array
#for row in array_2D:
    #print(row)
     
    #for elements in row:
      # print(elements)
#iterate the elemenyts whithout nexted loop
for elements in np.nditer(array_2D):
    print(elements)

# iterate the elements with inddx
for index, element in np.ndenumerate(array_2D):
    print (f"index: {index}, element : {element}")