# ### 10. A positive integer is entered through the keyboard, write a program to obtain the prime factors of the number. Modify the function suitability to obtain the prime factors recursively.
# 
# * Function: isPrime()
# * Summary: Determines the prime factors of a number 
# * Input: n
# * Output: prime factors

# In[81]:


def isPrime(n, i = 2): 
  

    if (n <= 2): 
        if(n == 2):
            print(n)
        else:
            return False
    if (n % i == 0): 
        return False
    if (i * i > n): 
        print(n) 
  

    return isPrime(n, i + 1) 
  
  

num=24

for i in range(2,num): 
    while((num % i) == 0):
        num=num/i
        isPrime(i)
