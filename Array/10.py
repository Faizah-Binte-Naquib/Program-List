# ### 10. Write a program to merge two arrays removing the duplicate elements.
# * Summary: Removes the duplicates between two arrays and merges them
# * Input: 
# * Output: outputs the updtaes merged array

# In[113]:


array1=[7,9,3,6,5,2,9,0,8,2] #input array 1
array2=[10,11,12,13,14,12,9,0,8,2] #input array 2

print("array 1:",array1)
print("array 2;",array2)

first_array=set(array1) #converts to set
second_array=set(array2) #converts to set

 #subtracts one from the other to remove the common elements
removing_duplicates_array2=second_array-first_array

#merges the updated array2 with array 1
first_array.update(removing_duplicates_array2) 

print("updated array:",list(first_array))