# ### 8. Write a program to find the common characters from two arrays.
# * Summary: Finds common characters between two arrays
# * Input: 
# * Output: outputs all the common characters 

# In[102]:


array1=[7,9,3,6,5,2,9,0,8,2] #input array 1
array2=[10,11,12,13,14,12,9,0,8,2] #input array 2
print("array 1:",array1)
print("array 2:",array2)
dict={}
count=0
for i in array1:
    for j in array2:
        if(i==j):
            count=count+1
    dict[i]=count
    count=0
for i in dict.items():
    if(i[1]>=1):
        print(i[0])
            
#print(array)