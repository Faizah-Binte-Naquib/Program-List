# ### 6. A prime integer is entered through the keyboard. Write a function to obtain the prime factors of this number. For example, prime factors of 24 are 2, 2, 2 and 3 whereas prime factor of 35 are 5 and 7.
# 
# * Function: find_prime()
# * Summary: Determines if prime or not
# * Input: number
# * Output: prints value if prime

# In[50]:


def find_prime(num):
    flag=0
    if(num==2):
        print(num)
    for i in range(2,num): 
        if ((num % i) == 0): 
            flag=2
            break  
        if(flag!=2):
            print(num)
        
        
num=24
for i in range(2,num): 
    while((num % i) == 0):
        num=num/i
        find_prime(i)
