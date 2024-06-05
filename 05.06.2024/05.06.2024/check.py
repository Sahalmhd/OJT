import numpy as np

array = np.array([10,20,12,15,14,17])
# np.whare (array== 20)
# whare is the methord we used to checke the perticular condition for fileter and condition

#elemet grate then is foe above array
elements = np.where(array>15)
print(array)
print(array[elements])