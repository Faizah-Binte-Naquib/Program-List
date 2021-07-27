# ### 14. Write a program to count the number of letters and words within a text.
# * Summary: Counts the total number of words and characters present in a string 
# * Input:
# * Output: 
#     1. Total number of words
#     2. Total number of characters 

# In[7]:


test_str = "A testing string"
print(test_str)

words=(test_str.split())
print("Number of words",len(words))

count=0
for i in test_str:
    count=count+1
    if(i==' '):
        count=count-1
        
print("Number of characters",count)
