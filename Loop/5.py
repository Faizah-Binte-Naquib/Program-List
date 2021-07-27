# <b>4. Write a program to determine all prime numbers within the range [a …b]
# where a & b are input through keyboard.</b>
#     
# * Summary: Determines prime number
# * Input: Take range input start and end
# * Output: all prime numbers withing range

# In[21]:


a= int(input("Enter lower range: "))  
b= int(input("Enter upper range: "))  
flag=1
for num in range(a,b+1): 
    flag=1
    if(num>1):  
        for i in range(2,num): 
            #print("num:",num)
            #print("i:",i)
            if ((num % i) == 0): 
                flag=2
                break  
        if(flag!=2):
            print(num)          
