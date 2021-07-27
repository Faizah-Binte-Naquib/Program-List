# ### 5. Write a program to find out the maximum, minimum, median and mode of an array of numbers.
# * Summary: Determines the maximum, minimum, median and mode of a given array
# * Input: 
# * Output: maximum, minimum, median and mode

# In[11]:


array=[7,9,3,6,5,2,9,0,8,2] #input array
print(array)
#Max
print("Maximum:",max(array))

#Min
print("Minimum:",min(array))

#Mean
sum=0
for i in array:
    sum=sum+i
mean=sum/len(array)
print("Mean:",mean)


# In[8]:


#Median
if(len(array)%2==0):
    middle_1=int(len(array)/2)
    middle_2=int(len(array)/2)+1
    median=(array[middle_1]+array[middle_2])/2
else:
    median=array[math.ceil(len(array)/2)]
print("Median:",median)


# In[9]:


#Mode
dict={}
count=0
for i in array:
    for j in array:
        if(i==j):
            count=count+1
    dict[i]=count
    count=0
print("Mode:",end=" ")
max_value = max(dict.values()) 
for i in dict.items():
    if(i[1]==max_value):
        print(i[0],end=" ")