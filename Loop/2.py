# <b>2. Write a program to determine the GCD (greatest common divisor) and
# LCM (least common multiple) of 3 numbers.</b>
# 
# * Summary: determines the gcd and lcm of three numbers 
# * Input: 3 numbers 
# * Output: gcd,lcm

# In[2]:


values=[]

for i in range(0,3):
    values.append(int(input("Enter a value for calculating GCD/LCM:")))
values.sort()

smallest=values[0]
greatest=values[2]
for i in range(1,smallest+1):
    if((values[0]%i==0)and(values[1]%i==0)and(values[2]%i==0)):
        gcd=i
print("GCD:",gcd)


while(True):
    if((greatest % values[0] == 0) and (greatest % values[1] == 0) and (greatest % values[2] == 0)):
        lcm = greatest
        break
    greatest += 1
print("LCM:",lcm)