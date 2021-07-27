# <b>8. A certain grade of steel is graded according to the following conditions:
# 1. Hardness must be greater than 60
# 2. Carbon content must be less than 0.7
# 3. Tensile strength must be greater than 5000
# <br>
# The grades are as follows:<br>
#     1. Grade is 10 if all three conditions are met<br>
#     2. Grade is 9 if condition (i) and (ii) are met<br>
#     3. Grade is 8 if condition (ii) and (iii) are met<br>
#     4. Grade is 7 if condition (i) and (iii) are met<br>
#     5. Grade is 6 if only one condition is met<br>
#     6. Grade is 5 if none of the conditions are met<br>
# <br>
# Write a program which will require the user to give values of hardness,
# carbon content and tensile strength of the steel under consideration and
# output the grade of the steel.</b><br>
# 
# * Summary:Determines the grade of a steel from given conditions
# * Input: 
#     1. hardeness of steel
#     2. carbon value of steel
#     3. tensile of steel
# * Output: grade

# In[25]:


hardness = float(input("What is the value of hardness:"))
carbon = float(input("What is the value of carbon:"))
tensile = float(input("What is the value of tensile:"))
if(hardness>60 and carbon<0.7 and tensile>5000):
    print("Grade: 10")
elif(hardness>60 and carbon<0.7):
    print("Grade: 9")
elif(carbon<0.7 and tensile>5000):
    print("Grade: 8")
elif(hardness>60 and  tensile>5000):
    print("Grade: 7")
elif(hardness>60 or carbon<0.7 or tensile>5000):
    print("Grade: 6")
else:
    print("Grade:5")