# <b>3. The length and height of a rectangle and radius of a circle are input through the keyboard. Write a program to find the area & perimeter of the rectangle and the area & circumference of the circle.</b>
# * Summary: Prints area and perimeter of a rectangle + prints area and circumference of a circle

# In[10]:


import math
length=float(input("Lenght of a rectangle:"))
height=float(input("Height of a rectangle:"))
radius=float(input("Radius of a circle:"))

rectangle_area=length*height
rectangle_perimeter=2*length+2*height
circle_area=math.pi*(radius**2)
circle_circumference=2*math.pi*radius

print("Area of rectangle:",rectangle_area)
print("Perimeter of rectangle:",rectangle_perimeter)
print("Area of circle:",circle_area)
print("Circumference of circle:",circle_circumference)
