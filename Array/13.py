# ### 13. Write a program to count the frequencies of each character present in a text. (In addition to alphabet letters, count also the space, tab and punctuation letters)
# * Summary: Counts the number of times a character apears in a string 
# * Input: string
# * Output: Count of all characters

# In[2]:


# initializing string 
test_str = "A testingstring"
print(test_str)

# of each element in string 
all_freq = {}
  
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
  


print ("Count of all characters:"+  str(all_freq))
