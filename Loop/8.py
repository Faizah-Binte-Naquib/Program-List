# <b>7. Write a program to find first n Fibonacci number where n is the input from user.</b>
# * Summary: Finds fibonacci number for first n terms
# * Input: n
# * Output: fibonacci number for n terms

# In[31]:


n=int(input("Enter value of n:"))
first=0
second=1
print(first,second,end=",")
for i in range(3,n+1):
    third=first+second
    print(third,end=",")
    first=second
    second=third
