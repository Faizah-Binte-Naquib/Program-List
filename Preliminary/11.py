# <b>11. If a 5 digit number is input through the keyboard, write a program to reverse the number.</b>
# * Summary: Takes a 5 digit number and reverses it

# In[80]:


num = int(input("Enter a 5 digit number:"))
num_1=num%10 #5th digit
num=((num-num%10)/10)
num_2=num%10 #4th digit
num=((num-num%10)/10)
num_3=num%10 #3rd digit
num=((num-num%10)/10)
num_4=num%10 #2nd digit
num=((num-num%10)/10) #1st digit
print(num_1*10000+num_2*1000+num_3*100+num_4*10+num*1)

