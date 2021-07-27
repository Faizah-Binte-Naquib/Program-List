# ### 18. Write a program to Multiply two matrices
# * Summary: Multiplies two matrices
# * Input: from the previous problem
# * Output: Product of two matrices

# In[13]:

import numpy as np
row = int(input("Enter the number of rows:"))
col = int(input("Enter the number of columns:"))

print("Array1-")
print("Enter values rowwise:")

array1=[]
array2=[]

for i in range(row):         
    temp =[]
    for j in range(col):     
         temp.append(int(input()))
    array1.append(temp)

print("Array2-")
print("Enter values rowwise:")

for i in range(row):         
    temp =[]
    for j in range(col):     
         temp.append(int(input()))
    array2.append(temp)
    

mul=array1*array2
print(mul)