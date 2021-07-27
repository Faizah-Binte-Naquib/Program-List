# ### 4. Deleting an element from an array.
# * Summary: Deletes an input element from a given array
# * Input: 
#     1. element
# * Output: updated array

# In[21]:


array=[7,9,3,6,5,2,9,0,8,2] #input array
print("Original Array:",array)
element=int(input("Enter value:"))
array.remove(element)
print("Updated Array:",array)