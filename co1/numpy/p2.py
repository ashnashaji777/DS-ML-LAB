import numpy as np
np_array=[]
n=int(input("enter the number of elements:"))
for i in range(0,n):
    element=int(input("enter element"))
    np_array.append(element)
                
print(np_array)
k=3
array1=np.sort(np_array)
print(k, "smallest elements of the array")
print(array1[:k])
