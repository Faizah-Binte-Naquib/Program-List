# <b>4. Write a program which will show the use of all built-in mathematical functions in C (eg : power, square root, logarithmic, trigonometric etc.)</b>
# 
# * Summary: Containes a list of basic built in mathmetical functions

# In[29]:


# Number-theoretic and representation functions
print("ceil:", math.ceil(1.56)) #ceiling of 1.56
print("floor:", math.floor(1.56)) #floor of 1.56
print("absolute value:",math.fabs(-10)) #absolute value of -10
print("gcd:",math.gcd(2,4))
print("mod:",math.fmod(113,2)) # 113 modulo 2


# In[38]:


#Power and logarithmic functions
print("exponential:",math.exp(2)) # e to the power 2
print("log:",math.log(10,2)) # log of 10 base 2
print("power:",math.pow(2,2)) #2 to the power 2


# In[44]:


#Trigonometric functions
x=60/180
print("cosine:",math.acos(x))
print("sine:",math.asin(x))
print("tan:",math.atan(x))
