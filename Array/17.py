# ### 17. Write a program to Add/Subtract two different Matrices, input from the user.
# 
# * Summary: Adds and subtracts two matrices 
# * Input:
#     1. numbe of rows
#     2. number of columns
#     3. matrix 1
#     4. matrix 2
# * Output: 
#     1. Summation of the two matrix 
#     2. Subtraction of one matrix from the other 

# In[11]:


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
    

sum=np.asarray(array1)+np.asarray(array2)
sub=np.asarray(array1)-np.asarray(array2)

print("Addition:",sum)
print("Subtraction:",sub)
