# 
# * Function: product()
# * Summary: finds product of two numbers
# * Input: a,b
# * Output: product
# _________________
# 
# * Function: main()
# * Summary: takes input of two numbers and print product
# * Input: a,b
# * Output: product

# In[52]:


def product(a,b):
    prod=a*b
    return prod
def main():
    a=float(input("Enter a float value:"))
    b=int(input("Enter an integer value:"))
    ans=product(a,b)
    print(ans)
main()