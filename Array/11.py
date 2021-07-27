# ### 11. Take a string as input and check whether it is a Palindrome. If it is not a palindrome, then add minimum no. of character after the string to convert it into a palindrome.
# * Summary: Checks to see if a string is palindrome, if not then converts it into one
# * Input: string
# * Output: 
#     1. States "palndrom" if string is palyndrom 
#     2. else prints the converted palindrom

# In[120]:


string=input("Enter a string:")
rev_string=""
def string_rev(string):
    rev_string=""
    for i in string:
        rev_string=i+rev_string
    return rev_string
    
rev_string=string_rev(string)   
if(string==rev_string):
    print("plaindrom")
else:
    for i in range(1,len(rev_string)):
        string=string+rev_string[i]
        if(string==string_rev(string)):
            break
        

print(string)