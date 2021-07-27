# ### 2. Inserting an element into a position of an array. The element and the insertion point are inputs from the user.
# * Summary: Insert an element in an array at any given index
# * Input: 
#     1. array
#     2. index number
# * Output: updated array

# In[10]:


string=[1,2,3,4,5,6,7] #input array
print("Existing String",string)
element=input("What to be inserted:")
index=int(input("Index at which to be inserted:"))
string.insert(index,element)
print("Updated String",string)