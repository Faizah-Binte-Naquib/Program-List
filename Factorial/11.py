# ### 11. Write a recursive function to obtain the first 25 numbers of a Fibonacci sequence. In a Fibonacci sequences the sum of two successive terms given the third term. Following are the first few term of the Fibonacci sequence: 1 1 2 3 5 8 13 21 34 55…
# 
# * Function: fibonacci()
# * Summary: finds fibonaci numbers recursively 
# * Input: n
# * Output: fibonacci numbers 

# In[3]:


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

nterms = 25


print("Fibonacci sequence:")
for i in range(nterms):
       print(fibonacci(i),end=" ")
