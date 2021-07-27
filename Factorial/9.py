# ### 9. A 5 digit positive integer is entered through the keyboard, write a function to calculate sum of digits of the 5 digit number 
# <b> 1. Using recursion</b> 
# <b> 2. Without using recursion</b>
# 
# * Function: rec_sum_of_digit()
# * Summary: finds summation recursively
# * Input: n
# * Output: sum
# 
# _____
# 
# * Function: nonrec_sum_of_digit()
# * Summary: finds summation non-recursively
# * Input: n
# * Output: sum

# In[69]:


def rec_sum_of_digit(n):
    if n == 0:
        return 0
    return (n % 10 + sum_of_digit(int(n / 10)))

def nonrec_sum_of_digit(n):
    sum = 0
    for i in range(0,n):
        a = int(n%10) #obtaining the last digit
        sum = sum + a #summing up the digits
        n = n / 10 #decreasing the number by one digit
    return (sum)

num = 12345
result = nonrec_sum_of_digit(num)
print("Sum of digits with nonrecursion", result)
result = rec_sum_of_digit(num)
print("Sum of digits with recursion", result)
