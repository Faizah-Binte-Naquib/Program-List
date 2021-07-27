# <b> 7. AUST grading policy is :<br>
# (i) 80 % marks or above is A+<br>
# (ii) 75% to 79% marks is A<br>
# (iii) 70% to 74% marks is A-<br>
# (iv) 65% to 69% marks is B+<br>
# (v) 60% to 64% marks is B<br>
# (vi) 55% to 59% marks is B-<br>
# (vii) 50% to 54% marks is C+<br>
# (viii) 45% to 49% marks is C<br>
# (ix) 40% to 44% marks is D<br>
# (x) Below 40% is F<br>
# Write a program which will take an input from user and calculate the grade of
# a student according to AUST grading policy based on that input.</b>
# 
#     
# * Summary: Determines the grade of a given score
# * Input: score
# * Output: grade

# In[22]:


score=float(input("Enter the score of a student:"))
if(score>=80):
    print("Grade:A+")
elif(score>=75 and score<=79):
    print("Grade:A")
elif(score>=70 and  score<=74):
    print("Grade:A-")
elif(score>=65 and  score<=69):
    print("Grade:B+")
elif(score>=60 and  score<=64):
    print("Grade:B")
elif(score>=55 and  score<=59):
    print("Grade:B-")
elif(score>=50 and  score<=54):
    print("Grade:C+")
elif(score>=45 and  score<=49):
    print("Grade:C")
elif(score>=40 and  score<=44):
    print("Grade:D")
elif(score<40):
    print("Grade:F")
