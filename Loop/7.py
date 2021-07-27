# <b> 6. Write a program to find out first n perfect number where n is the input from user.</b>
# * Summary: Determines perfect numbers
# * Input: n
# * Output: Perfect numbers within n range

# In[27]:


n=int(input("Enter value of n:"))
for i in range(1,n+1):
    sum=0
    for j in range(1,i):
        if(i%j==0):
            sum=sum+j
    if(sum==i):
        print(i)
