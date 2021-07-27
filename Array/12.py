# ### 12. Write a program to merge two sorted arrays.
# * Summary: Merges and sorts two arrays
# * Input: 
# * Output: opdated merged array

# In[1]:


test_list1 = [1, 5, 6, 9, 11]
test_list2 = [3, 4, 7, 8, 10]
 print(test_list1)
 print(test_list2)
# to combine two sorted lists
res = sorted(test_list1 + test_list2)
  
print ("The combined sorted list is : " + str(res))
