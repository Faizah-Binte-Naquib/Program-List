# <b> 4. Any integer is input through keyboard. Write a program to find out whether it is an odd number or even number. </b>
# * Summary: Determines if number is odd or even
# * Input: number
# * Output: print odd or even

# In[7]:


integer = int(input("Enter any integer:"))
if(integer%2==0):
    print("Even number")
else:
    print("Odd number")

