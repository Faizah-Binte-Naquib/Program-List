# <b>10. Write a program to calculate how many 5 digit numbers can be created if the following terms apply :
# (i) the leftmost digit is even
# (ii) the second digit is odd
# (iii) the third digit is a non even prime
# (iv) the fourth and fifth are two random digits not used before in the number.</b>
# 
# * Summary: Determines all possible 5 digit numbers for given conditions
# * Input:
# * Output: total numbers

# In[154]:


flag=1
count=0
for i in range(10000,100000):
    num_str=str(i)
    if(int(num_str[0])%2==0):
        if(int(num_str[1])%2!=0):
            for j in range(1,int(num_str[2])):
                if(int(num_str[2])%j==0 and int(num_str)!=2):
                    flag=2
            if(flag==1):
                if(int(num_str[3])!=int(num_str[0]) and int(num_str[3])!=int(num_str[1]) and int(num_str[3])!=int(num_str[2])):
                    if(int(num_str[3])!=int(num_str[0]) and int(num_str[3])!=int(num_str[1]) and int(num_str[3])!=int(num_str[2]) and int(num_str[4])!=int(num_str[3])):
                        count=count+1
    flag=1
print(count)
