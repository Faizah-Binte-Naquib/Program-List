# ### 2. Write a function power(a,b) to calculate the value of a raised to b. 
# * Function: power()
# * Summary: Finds a^b
# * Input: a and b
# * Output: a^b

# In[16]:


def power(n,p):
    if p==0:
        return 1
    elif p==1:
        return n
    else:
        return n*power(n,p-1)

print(power(3,4))

