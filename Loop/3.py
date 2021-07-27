# <b>3. Find out the sum of each of the following series. n is the input from user
# for series</b>
# * Summary: Contains 6 different series, determines the summation of each
# * Input:
# * Output: Summation of Series

# In[4]:


#3 + 11 + 19 + … + 1691.
start=3
end=int(input())
sum=0
flag=1
while(flag==1):
    sum=sum+start
    start=start+8
    if(start==end):
        flag=2
        break
print(sum)