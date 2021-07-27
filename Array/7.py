# ### 7. Write a program to delete duplicate elements from an array.
# * Summary: Finds the duplicate of a term and deletes it
# * Input: 
# * Output: updated array

# In[99]:


array=[7,9,3,6,5,2,9,0,8,2] #input array
print(array)
dict={}
count=0
for i in array:
    for j in array:
        if(i==j):
            count=count+1
    dict[i]=count #stores the number of times an element is found, and the element is taken as key
    count=0
for i in dict.items():
    if(i[1]>=2):
        for j in range(1,i[1]):
            array.remove(i[0])
            
print(array)