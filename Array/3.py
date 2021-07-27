# ### 3. Inserting a number/character into the proper position of an array which is sorted in ascending/descending order.
# 
# * Summary: Sorts an array in ascending order and places a given number in such a manner that the order is maintained
# * Input: 
#     1. array
#     2. number
# * Output: updated array

# In[6]:


array=[7,9,3,6,5,2,9,0,8,2] #input array
array.sort()
element=int(input("Enter value:"))
index=0
for i in array:
    if(element<=i):
        array.insert(index,element)
        break
    index=index+1
print(array)