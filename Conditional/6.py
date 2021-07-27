# <b>6. A five digit number is entered through the keyboard. Write a program to obtain the reverse number and to determine whether the original numbers are equal or not.</b>
# * Summary: Determines if a number and its reverse are equal or not
# * Input: 5 digit number 
# * Output: equal or not equal

# In[15]:


num = int(input("Enter a 5 digit number:"))
n=num
num_1=num%10 #5th digit
num=((num-num%10)/10)
num_2=num%10 #4th digit
num=((num-num%10)/10)
num_3=num%10 #3rd digit
num=((num-num%10)/10)
num_4=num%10 #2nd digit
num=((num-num%10)/10) #1st digit
n_rev=(num_1*10000+num_2*1000+num_3*100+num_4*10+num*1)
if(n==n_rev):
    print("Equal")
else:
    print("Not Equal")
