# <b>1. x and n are input through keyboard. Write a program to compute x^n , n! ,
# nCr , nPr</b>
# * Summary: computes power, factorial, permutation and combination
# * Input: x and n
# * Output: power, factorial, permutation and combination

# In[9]:


x=int(input("Enter value of x:"))
n=int(input("Enter value of n:"))
p=1
for i in range(0,n):
    p=p*x
print("x^n",p)


# In[10]:


p=1
for i in reversed(range(1,n+1)):
     p=p*i
print("n!",p)


# In[24]:


r=x
n_fact=1
r_fact=1
nr_fact=1
#nCr = n!/r!(n-r)!
#nPr = n!/(n-r)!
for i in reversed(range(1,n+1)):
     n_fact=n_fact*i
for i in reversed(range(1,r+1)):
     r_fact=r_fact*i
nr= n-r
for i in reversed(range(1,nr+1)):
     nr_fact=nr_fact*i
        
C= n_fact/(r_fact*nr_fact)
P= n_fact/nr_fact

print("Combination:",C)
print("Permutation:",P)