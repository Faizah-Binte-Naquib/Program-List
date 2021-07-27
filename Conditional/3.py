# <b> 3. If cost price and selling price of an item is input through the keyboard, write a program to determine whether the seller has made profit or incurred loss. Also determine how much profit he made or loss he incurred. </b>
# * Summary: Determines incurred profit or loss
# * Input: cost and selling price
# * Output: profit or loss

# In[6]:


cost_price=float(input("Cost price of an item:"))
selling_price=float(input("Selling price of an item:"))
if(cost_price>selling_price):
    print("loss:",cost_price-selling_price)
else:
    print("profit:",selling_price-cost_price)

