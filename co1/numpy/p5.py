import numpy as np
"""array=[]
n=int(input("enter the number of elements"))
for i in range(0,n):
      element=int(input("enter the element"))
      array.append(element)"""
array=np.array([1,5,3,0,44,2,0,3])
print(array) 
res = np.where(array == [0])
print("indices having 0",res)                 
