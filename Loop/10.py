# <b>9. Write a program to print out all Armstrong numbers between 1 and 10000. If sum of cubes of each digit of the number is equal to the number itself, then the number is called an Armstrong number. For example, 153 = (1x1x1) + (5x5x5) + (3x3x3).</b>
# * Summary: Determines all the Armstrong numbers in a range
# * Input:
# * Output: Armstrong numbers 

# In[148]:


for i in range(2,10001):
    num_str=str(i)
    for num in num_str:
        sum=sum+math.pow(int(num),3)
    if(sum==i):
        print(i)
    sum=0
