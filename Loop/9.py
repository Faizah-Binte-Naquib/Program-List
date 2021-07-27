# <b>8. Write a program to show the following triangle/rectangle of ‘*’s or numbers. Take n as input from user to determine the number of rows of the structure. (eg: n = 5 )</b>
# 
# * Summary: Prints different patterns
# * Input: n
# * Output: patterns

# In[69]:


n=int(input("Enter value of n:"))
num_stars=1
num_space=n-1
for i in reversed(range(1,n+1)):
    for j in range(0,num_space):
        print(" ",end="")
    for j in range(0,num_stars):
        print("*",end="")
    num_stars=num_stars+2
    num_space=num_space-1
    print("\n")


# In[68]:


n=int(input("Enter value of n:"))
num_stars=1
num_space=n-1
for i in (range(1,n+1)):
    if(i<n):
        for j in range(0,num_space):
            print(" ",end="")
        for j in range(0,num_stars):
            if(j==0 or j==num_stars-1):
                print("*",end="")
            else:
                print(" ",end="")
        num_stars=num_stars+2
        num_space=num_space-1
        print("\n")
    else:
        for j in range(0,num_stars):
            print("*",end="")


# In[75]:


import math
n=int(input("Enter value of n:"))
num_stars=1
num_space=n-1
for i in (range(1,n+1)):
    for j in range(0,num_space):
        print(" ",end="")
    for j in range(0,math.ceil(num_stars/2)):
        print(j+1,end="")
    for k in reversed(range(0,num_stars-math.ceil(num_stars/2))):
        print(k+1,end="")
            
    num_stars=num_stars+2
    num_space=num_space-1
    print("\n")


# In[80]:


n=int(input("Enter value of n:"))
for i in (range(1,n+1)):
    for j in (range(1,n+1)):
        print("*",end="")
    print("\n")


# In[95]:


n=int(input("Enter value of n:"))
for i in (range(1,n+1)):
    if(i==1 or i==n):
        for j in (range(1,math.ceil(n/2)+1)):
            print(j,end="")
        for j in reversed(range(1,n-math.ceil(n/2)+1)):
            print(j,end="")
        print("\n")
    else:
        for j in (range(1,n+1)):
            if(j==1 or j==n):
                print("1",end="")
            else:
                print(" ",end="")
        print("\n")
            
        


# In[103]:


n=int(input("Enter value of n:"))
num_stars=1
num_space=n-1
for i in reversed(range(1,n+1)):
    for j in range(0,num_space):
        print(" ",end="")
    for j in range(0,num_stars):
        print("*",end="")
    num_stars=num_stars+2
    num_space=num_space-1
    print("\n")
    
#initial space and stars after first phase
num_stars=num_stars-2
num_space=0

#this loop is the same as the first, just the starts and spaces were swapped
for i in reversed(range(1,n+1)):
    for j in range(0,num_space):
        print(" ",end="")
    for j in range(0,num_stars):
        print("*",end="")
    num_stars=num_stars-2
    num_space=num_space+1
    print("\n")


# In[108]:


n=int(input("Enter value of n:"))
num_stars=1
num_space=n-1
for i in (range(1,n+1)):
    for j in range(0,num_space):
        print(" ",end="")
    for j in range(0,num_stars):
        if(j==0 or j==num_stars-1):
            print("*",end="")
        else:
            print(" ",end="")
    num_stars=num_stars+2
    num_space=num_space-1
    print("\n")
    
#initial space and stars after first phase
num_stars=num_stars-2
num_space=0

#this loop is the same as the first, just the starts and spaces were swapped
for i in (range(1,n+1)):
    for j in range(0,num_space):
        print(" ",end="")
    for j in range(0,num_stars):
        if(j==0 or j==num_stars-1):
            print("*",end="")
        else:
            print(" ",end="")
    num_stars=num_stars-2
    num_space=num_space+1
    print("\n")


# In[110]:


import math
n=int(input("Enter value of n:"))
num_stars=1
num_space=n-1
for i in (range(1,n+1)):
    for j in range(0,num_space):
        print(" ",end="")
    for j in range(0,math.ceil(num_stars/2)):
        print(j+1,end="")
    for k in reversed(range(0,num_stars-math.ceil(num_stars/2))):
        print(k+1,end="")
            
    num_stars=num_stars+2
    num_space=num_space-1
    print("\n")
    
#initial numbers of space and numbers after first phase
num_stars=num_stars-2
num_space=0

#this loop is the same as the first, just the starts and spaces were swapped
for i in (range(1,n+1)):
    for j in range(0,num_space):
        print(" ",end="")
    for j in range(0,math.ceil(num_stars/2)):
        print(j+1,end="")
    for k in reversed(range(0,num_stars-math.ceil(num_stars/2))):
        print(k+1,end="")
            
    num_stars=num_stars-2
    num_space=num_space+1
    print("\n")


# In[131]:


n=int(input("Enter value of n:"))

#Initial number of spaces and stars 
num_stars=2*n-1
num_space=0

#first loop
for i in reversed(range(1,n+1)):
    for j in range(0,num_space):
        print(" ",end="")
    for j in range(0,num_stars):
        print("*",end="")
    num_stars=num_stars-2
    num_space=num_space+1
    print("\n")
    
#Initial number of spaces and numbers after first phase 
num_stars=2
num_space=n-1

#this loop is the same as the first, just the starts and spaces were swapped
for i in reversed(range(1,n)):
        for j in range(0,num_space):
            print(" ",end="")
        for j in range(0,num_stars):
            print("*",end="")
        num_stars=num_stars+2
        num_space=num_space-1
        print("\n")


# In[132]:


import math
n=int(input("Enter value of n:"))
num_stars=2*n-1
num_space=0
for i in (range(1,n+1)):
    for j in range(0,num_space):
        print(" ",end="")
    for j in range(0,math.ceil(num_stars/2)):
        print(j+1,end="")
    for k in reversed(range(0,num_stars-math.ceil(num_stars/2))):
        print(k+1,end="")
            
    num_stars=num_stars-2
    num_space=num_space+1
    print("\n")
    
#initial number of spaces and numbers after first phase
num_stars=3
num_space=n-2

#this loop is the same as the first, just the starts and spaces were swapped
for i in (range(1,n)):
    for j in range(0,num_space):
        print(" ",end="")
    for j in range(0,math.ceil(num_stars/2)):
        print(j+1,end="")
    for k in reversed(range(0,num_stars-math.ceil(num_stars/2))):
        print(k+1,end="")
            
    num_stars=num_stars+2
    num_space=num_space-1
    print("\n")