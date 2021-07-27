# ## 15. Write a program which will search for a substring within a string.
# * Summary: Searches for a substring in a string 
# * Input: 
# * Output: 
#     1. Prints found if found
#     2. else nothing
# 

# In[8]:


test_str = "A testing string"

word="string"
sentence=(test_str.split())

for i in sentence:
    if(i==word):
        print('found')

