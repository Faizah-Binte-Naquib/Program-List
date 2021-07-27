# ### 9. Take a string as input and print the characters in reverse order. Don’t use any built in string function.
# * Summary: Reverses a given string 
# * Input: string
# * Output: outputs the string in reverse order

# In[105]:


string=input("Enter a string:")
rev_string=""
for i in string:
    rev_string=i+rev_string
print(rev_string)
