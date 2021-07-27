# <b> 5. According to Gregorian calendar, it was Monday on the date 01/01/1900. If any year is input through the keyboard write a program to find out what is the day on 1st January of this year. </b>
# 
# * Summary: Determines the day of a given date for Greogorian calender
# * Input: 
# * Output: day

# In[14]:


year_diff=365*(2021-1900)
day=year_diff%7
if(day==0):
    print("Monday")
elif(day==1):
    print("Tuesday")
elif(day==2):
    print("Wednesday")
elif(day==3):
    print("Thursday")
elif(day==4):
    print("Friday")
elif(day==5):
    print("Saturday")
elif(day==6):
    print("Sunday")

