# ### 16. Take n numbers as input from the user. Find out their GCD (Greatest Common Divisor) and LCM (Least Common Multiple).
# * Summary: Determines LCM and GCD 

# * Function: find_gcd
# * Input: two numbers taken from the array
# * Output: prints gcd

# In[4]:


def find_gcd(num1,num2):
    # the greate number is set as num while the other is set as denominator
    if(num1>num2):
        num=num1
        den=num2
    else:
        num=num2
        den=num1
        
    #the remainder obtained from the num and denominator is stored 
    rem=num%den
    
    #is performed until remainder=0 is obtained
    while(rem!=0):
        num=den
        den=rem
        rem= num%den
        
    gcd = den

    return gcd


array = [2, 4, 6, 8, 16]
 
num1 = array[0]
num2 = array[1]
gcd = find_gcd(num1, num2)
 
for i in range(2, len(array)):
    gcd = find_gcd(gcd, array[i])
     
print(gcd)


def find_lcm(num1,num2):
    # the greate number is set as num while the other is set as denominator
    if(num1>num2):
        num=num1
        den=num2
    else:
        num=num2
        den=num1
        
    #the remainder obtained from the num and denominator is stored 
    rem=num%den
    
    #is performed until remainder=0 is obtained
    while(rem!=0):
        num=den
        den=rem
        rem= num%den
        
    gcd = den
    
    #converting gcd to lcm
    lcm = int(int(num1*num2)/int(gcd))
    return lcm
     
array = [2, 7, 3, 9, 4]
 
num1 = array[0]
num2 = array[1]
lcm = find_lcm(num1, num2)
 
for i in range(2, len(array)):
    lcm = find_lcm(lcm, array[i])
     
print(lcm)