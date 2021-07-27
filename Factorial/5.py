# ### 5. Any year is entered through the keyboard. Write a function to determine whether the year is a leap year or not.
# * Function: leap year
# * Summary: determines if leap year or not
# * Input: year
# * Output: Leap year of not a leap year

# In[18]:


year=int(input("Enter a year:"))
def leap_year(year):
    if(year%4==0 & year%100==0 and year%400==0):
        print("Leap Year")
    else:
        print("Not a Leap Year")
leap_year(year)
