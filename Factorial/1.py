#!/usr/bin/env python
# coding: utf-8

# ### 1. Write a function to calculate the factorial value of any integer entered through the keyboard.
# * Function: factorial()
# * Summary: Finds factorial of an integer
# * Input: n
# * Output: factorial

# In[12]:


def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)

num=int(input("Enter a value:"))
print("The factorial is:",factorial(num))
