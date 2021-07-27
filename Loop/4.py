# <b>3. Find out the sum of each of the following series. n is the input from user
# for series</b>
# * Summary: Contains 6 different series, determines the summation of each
# * Input:
# * Output: Summation of Series

# In[4]:


#3 + 11 + 19 + … + 1691.
start=3
end=int(input("Enter value of n:"))
sum=0
flag=1
while(flag==1):
    sum=sum+start
    start=start+8
    if(start==end):
        flag=2
        break
print(sum)

# In[49]:


#7 + 20 + 33 + … ( up to 100 th term )
start=7
sum=0
for i in range(1,101):
    sum=sum+start
    start=start+13

print(sum)    


# In[54]:


#5 – 11 + 17 - … (up to 75 th term )
start=5
sum=0
for i in range(1,4):
    if(i%2!=0):
        sum=sum+start
        start=start+6
    else:
        sum=sum-start
        start=start+6

print(sum)   


# In[2]:


#1 + ( 1 + 2 ) + ( 1 + 2 + 3 ) + … + ( 1 + 2 + 3 + … + n )
sum=0
start=1
n=int(input("Enter value of n:"))
for i in range(0,n):
    sum=sum+start
    for i in range(1,start):
        sum=sum+i
    start=start+1
    
print(sum)    


# In[12]:


# 1 +(2^2)/2!+(3^2)/3!+ … +(n^2)/n!
sum=0
start=1
new_num=1
p=1
n=int(input("Enter value of n:"))
for i in range(1,n+1):
    if(i>1):
        for i in reversed(range(1,start+1)):
            p=p*i
        new_num= (start**2)/p
    sum=sum+new_num
    start=start+1
print(sum)


# In[14]:


#2 * 7 * 12 * … * 37
start=2
end=37
sum=1
flag=1
while(flag==1):
    sum=sum+start
    start=start+5
    if(start==end):
        flag=2
        break
print(sum)
