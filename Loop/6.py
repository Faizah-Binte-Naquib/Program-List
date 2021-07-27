# 
# <b>5. Construct the following table. Here n is input from the user.
# </b>
# <img src="1.jpg">
# * Summary: Constructs the given table
# * Input: n
# * Output: table

# In[24]:


n=int(input("Enter value of n:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i*j, end =" ")
    print("\n")
   
