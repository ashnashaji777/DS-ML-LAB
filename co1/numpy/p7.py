import numpy as np
row=int(input("enter the no of row:"))
colomn=int(input("enter the no of coloumns:"))
array1=np.empty((row,colomn))
for i in range(row):
    for j in range(colomn):
        value1=float(input(f"enter the value for element at{i,+1}row and {j+1} coloumn"))
        array1[i,j] =value1

#row2=int(input("enter the no of rows of array2:"))
#colomn2=int(input("enter the no of coloumns of array2:"))
array2=np.empty((row,colomn))
for i in range(row):
    for j in range(colomn):
        value2=float(input(f"enter the value for element at{i,+1}row and {j+1} coloumn"))
        array2[i,j] =value2
sum= array1 + array2
# Perform element-wise subtraction
difference = array1 - array2

# Perform element-wise multiplication
product = array1 * array2

# Perform element-wise division
division = array1 / array2

# Display the results
print("Array 1:", array1)
print("Array 2:", array2)
print("Element-wise Addition:", sum)
print("Element-wise Subtraction:", difference)
print("Element-wise Multiplication:", product)
print("Element-wise Division:", division)
