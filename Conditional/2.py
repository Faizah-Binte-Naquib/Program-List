# <b>2. Take a year as input and determine whether it is a leap year.</b>
# * Summary: Determines leap year
# * Input: year
# * Output: prints leap year if is leap year

# In[5]:


year=int(input("Enter a year:"))
if(year%4==0 & year%100==0 and year%400==0):
    print("Leap Year")
