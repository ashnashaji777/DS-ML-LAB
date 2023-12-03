import numpy as np
row1=int(input("enter the no of rows of array1:"))
colomn1=int(input("enter the no of coloumns of array1:"))
array1=np.empty((row1,colomn1))
for i in range(row1):
    for j in range(colomn1):
        value1=float(input(f"enter the value for element at{i,+1}row and {j+1} coloumn"))
        array1[i,j] =value1
trace1=np.trace(array1)
print("array1:",array1)
print("sum of diagonal elements:",trace1)
