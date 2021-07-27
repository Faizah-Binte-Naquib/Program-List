# <b>9. If marks obtained by a student in 5 different subjects are input from keyboard, find out the aggregate marks and percentage marks obtained by the student.</b>
# 
# * Summary: Totak and average marks obtained by 5 students 

# In[62]:


sub1=float(input("Enter marks of subject 1:"))
sub2=float(input("Enter marks of subject 2:"))
sub3=float(input("Enter marks of subject 3:"))
sub4=float(input("Enter marks of subject 4:"))
sub5=float(input("Enter marks of subject 5:"))
total_marks= sub1+sub2+sub3+sub4+sub5
perc_marks= total_marks*(1/100)
print("Aggregate marks",total_marks) 
print("Percentage marks", perc_marks)
