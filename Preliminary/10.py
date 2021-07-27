# <b>10. If a 5 digit number is input through the keyboard, write a program to calculate and print the sum of its digits.</b>
# * Summary: Takes a 5 digit number and calculates the sum of its digits 

# In[77]:


num=int(input("Enter a 5 digit number:"))
num_1=num%10 #5th digit
num=((num-num%10)/10)
num_2=num%10 #4th digit
num=((num-num%10)/10)
num_3=num%10 #3rd digit
num=((num-num%10)/10)
num_4=num%10 #2nd digit
num=((num-num%10)/10) #1st digit
print(num_1+num_2+num_3+num_4+num)

