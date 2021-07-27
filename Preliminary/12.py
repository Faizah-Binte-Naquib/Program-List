# <b>12. If a 4 digit number is input through the keyboard, write a program to obtain the sum of the first and last digit of this number.</b>
# * Summary: Takes a 4 digit number, finds the sum of the first and last digit

# In[82]:


num = int(input("Enter a 4 digit number:"))
num_1=num%10 #4th digit
num=((num-num%10)/10)
num_2=num%10 #3rd digit
num=((num-num%10)/10)
num_3=num%10 #2nd digit
num=((num-num%10)/10) #1st digit
print(num_1+num)

