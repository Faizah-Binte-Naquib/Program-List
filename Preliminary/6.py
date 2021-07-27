# <b>6. The distance between AUST main campus and Rajshahi campus (in km) is input through keyboard. Write a program to convert and print this distance in meters, feet, inches and centimeters</b>
# 
# * Summary: Converts distance into m, ft, inch and cm

# In[51]:


dist=  float(input("Enter distance between AUST and Rajshahi campus:"))
print("Distance in meter",dist*1000)
print("Distance in feet",dist*3280.84)
print("Distance in inches",dist*39370.1)
print("Distance in centimeter",dist*1000000)
