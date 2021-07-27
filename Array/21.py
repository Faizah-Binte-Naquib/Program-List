# ### 21. Write a program to construct a nxn magic square
# * Summary: Constructs a nxn magic square (Brute Force Approach)
# * Input: 
# * Output: nxn magic square

# In[98]:


n=3

#formula to determine the sum value for the respective value of n
all_sum= n*((n**2)+1)/2
flag=0
a=[]

while(flag!=n*3):
    A = np.random.randint(all_sum, size=(n,n))
    
    #checks two see if this random matrix is unique 
    for i in a:
        if np.array_equal(i,A): 
            print('')
        else:
            flag=0
            
            #checks to see if each sum of row is equal to all_sum
            for i in A.sum(0):
                if(i==all_sum):
                    flag=flag+1
            
             #checks to see if each sum of column is equal to all_sum
            for i in A.sum(1):
                if(i==all_sum):
                    flag=flag+1
                    
            #checks to see if each sum of diagonals is equal to all_sum
            if(np.trace(A)==all_sum):
                flag=flag+n
            a.append(A)
            
print()