# <b>1. Two numbers are input through keyboard. Write a program to find out the maximum and minimum of these 2 numbers.</b>
# * Summary: Finds the maximum and minimum of two numbers
# * Input: two numbers
# * Output: maximum and minimum values

# In[1]:


num_1=float(input("Enter one number:"))
num_2=float(input("Enter another number:"))
if(num_1>num_2):
    print("Max number:",num_1)
    print("Min number:",num_2)
else:
    print("Max number:",num_2)
    print("Min number:",num_1)
