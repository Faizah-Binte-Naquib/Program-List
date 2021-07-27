# <b>8. Two numbers are input through the keyboard into two locations A and B. Write a program to interchange the contents of A and B.</b>
# * Summary: Swap two numbers

# In[54]:


A= int(input("Enter number:"))
B= int (input("Enter another number"))
temp=A
A=B
B=temp
print("Now A and B are:", A,B)
