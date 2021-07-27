# ### 1. Write a program to search for an element from an array input from the user.
# * Summary: Finds a specific character in a given string
# * Input: 
#     1. string
#     2. character
# * Output: Found or None

# In[5]:


string=input("Enter an array:")
element=input("Enter an element you are willing to find:")
for i in string:
    if(element==i):
        print("Found")
        break
