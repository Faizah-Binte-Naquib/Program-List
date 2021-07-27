# ### 6. Find k-th maximum and k-th minimum from an array.
# * Summary: Finds the kth minimum and maximum value in an array
# * Input: k
# * Output: kth minimum and kth maximum term

# In[81]:


arr=[7,10,4,3,20,15] #input array
print(arr)
k=int(input("Enter value of k:"))
asc_arr=sorted(arr)
desc_arr=sorted(arr,reverse=True)
print("Kth min term",asc_arr[k-1])
print("Kth max term",desc_arr[k-1])