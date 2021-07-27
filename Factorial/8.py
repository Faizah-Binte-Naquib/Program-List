# ### 8. Write a program which receives 5 integers and returns the sum , average and standard deviation of these numbers. Call this function from main() and print the results in main().
# 
# * Function: func()
# * Summary: finds sum, average and standard deviation
# * Input: a,b,c,d,e
# * Output: sum, average and standard deviation
# 
# ____
# 
# * Function: main()
# * Summary: takes input of five digit and prints their sum, avg, standard deviation
# * Input: a,b,c,d,e
# * Output: prints sum, average and standard deviation

# In[64]:


import math
def func(a,b,c,d,e):
    sum=a+b+c+d+e

    avg=sum/5

    sd= math.sqrt((pow(a-avg,2)+pow(b-avg,2)+pow(c-avg,2)+pow(d-avg,2)+pow(e-avg,2))/5)
    return sum,avg,sd
                                          
def main():
    a=int(input("Enter a first value:"))
    b=int(input("Enter a second value:"))
    c=int(input("Enter a third value:"))
    d=int(input("Enter a fourth value:"))
    e=int(input("Enter a fifth value:"))
    
    tuple=func(a,b,c,d,e)
    print("Sum is",tuple[0])
    print("Avg is",tuple[1])
    print("Standard deviation is",tuple[2])


# In[65]:


main()