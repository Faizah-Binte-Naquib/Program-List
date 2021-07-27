# <b>5. Rahim’s basic salary is input through the keyboard. His House rent allowance is 30% of basic salary and medical allowance is 5% of basic salary. He gets extra 1000 tk as technical allowance. Write a program to calculate his gross salary and print the result.</b>
# 
# * Summary: Determines the gross salary of the given person

# In[47]:


salary=float(input("Rahim's basic salary:"))
rent= (salary*(30/100))
med= (salary*(5/100))
gross_salary= salary+rent+med+1000
print(gross_salary)

