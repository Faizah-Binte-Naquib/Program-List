# <b>7. Temperature of a city in Fahrenheit degrees is input through the keyboard. Write a program to convert this temperature into centigrade degrees.</b>
# 
# * Summary: Converts Fahrenheit to Centigrade

# In[53]:


f= float(input("Enter Temperature in farenheit:"))
c=(f-32)*(5/9)
print("Temperature in centigrade:", c)
