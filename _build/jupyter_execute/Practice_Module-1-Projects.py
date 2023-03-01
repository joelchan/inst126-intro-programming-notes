#!/usr/bin/env python
# coding: utf-8

# # Practice: Module 1 Project (Conditional Functions)
# 
# ## 1: Traffic light timer
# 
# Two main considerations:
# 1. Rush hour or not (if rush hour, then we use 6 second cycles, otherwise we use 9)
# 2. Weekends or not (if weekends, then the rush hour rule doesn't apply, and we just use 9)

# In[1]:


def traffic_light_seconds(isRushHour, isWeekend):
    if isWeekend == False and isRushHour == True:
        return 6
    else:
        return 9
    
def traffic_light_seconds(isRushHour, isWeekend):
    if not isWeekend and isRushHour:
        return 6
    else:
        return 9


# In[2]:


a = 5
print(a)
a = a + 2
print(a)


# In[3]:


# run
rush = True
weekend = True
traffic_light_seconds(isRushHour=rush, isWeekend=weekend)


# In[4]:


# run
r = True
w = False
traffic_light_seconds(isRushHour=r, isWeekend=bw)


# In[14]:


traffic_light_seconds(True, False)


# 1. What are the names of the arguments in the function call?
# 2. What are the names of the parameters?
# 3. What are the value types of the parameters?
# 4. What is the value type of the return value?
# 5. What is the Boolean expression?
# 6. What comparison operators are used?
# 7. What Boolean/logical operators are used?
# 8. What conditional pattern is being used here?

# ## 2: Shipping calculator
# 
# Write a function called shipping_calculator that calculates the shipping cost based on the weight of the package and the destination. If the package is being shipped within the US and weighs less than or equal to 10 pounds, the shipping cost is \\$10. If the package is being shipped within the US and weighs more than 10 pounds, the shipping cost is \\$20. If the package is being shipped internationally and weighs less than or equal to 10 pounds, the shipping cost is \\$20. If the package is being shipped internationally and weighs more than 10 pounds, the shipping cost is \\$40.

# In[7]:


# define v1
def shipping_calculator(destination, weight):
    # domestic, light
    if destination == "US" and weight <= 10:
        return 10
    # international, heavy
    elif destination != "US" and weight > 10:
        return 40
    # domestic heavy and international light
    # i'm lazy to write out the Boolean expression :P
    else:
        return 20
    
# define v2
def shipping_calculator(destination, weight):
    # domestic, light
    if destination == "US":
        if weight <= 10:
            return 10
        else:
            return 20
    # international, heavy
    else:
        if weight <= 10:
            return 20
        else:
            return 40


# In[11]:


# run
d = "US"
w = 5
shipping_calculator(d, w)


# 1. What are the names of the arguments in the function call?
# 2. What are the names of the parameters?
# 3. What are the value types of the parameters?
# 4. What is the value type of the return value?
# 5. What are the Boolean expressions?
# 6. What comparison operators are used?
# 7. What Boolean/logical operators are used?
# 8. What conditional pattern is being used here?

# ## 3: Interest rate calculator for a mortgage loan.
# 
# Three main considerations:
# 1. `loanLength`: 15 starts at 7; 30 starts at 8
# 2. `creditScore` (int) 0 to 850 - exceptional (800 and up) applies a 10% reduction to the interest rate (e.g., 7 would go down to 6.3); very good (740 to 799) applies a 5% reduction, and good (670-739) applies a 2.5% reduction
# 3. `isSecured`: if True, then we get a flat 1 percentage point reduction of the interest rate after considering life of loan and credit score.
# 
# Returns an `float` that specifies the interest rate percentage as a function of the input params.

# In[17]:


# define 
def interest_rate(loanLength, creditScore, isSecured):
    
    # loanLength consideration
    if loanLength <= 15:
        rate = 7
    else:
        rate = 8
    
    # creditScore consideration
    if creditScore >= 800:
        rate = rate*0.9
    elif creditScore >= 740:
        rate = rate*0.95
    elif creditScore >= 670:
        rate = rate*0.975
    
    # isSecured consideration
    if isSecured:
        rate = rate-1
    
    return rate


# In[18]:


# run
l = 15
c = 700
s = True
interest_rate(l, c, s)


# ## 4: Travel caller for basketball
# 
# `is_traveling()` returns `True` or `False`, depending on:
# 1. `stepCount`: more than 2 = Travel (though subject to gather step and pivot considerations)
# 2. `gatherStep` (True or False). If True, subtract 1 from step count before deciding if it's a travel.
# 3. `isPivoting` (True or False). If True, then call no travel, regardless of `stepCount`

# In[19]:


# define
def is_traveling(stepCount, hasGatherStep, isPivoting):
    # if you're pivoting, nothing else matters, it's not a travel
    if isPivoting:
        return False
    # otherwise
    else:
        # if you're gather-stepping
        if hasGatherStep:
            # we subtract 1 from your stepcount
            # and check if it's greater than 2
            return stepCount - 1 > 2
        # otherwise
        else:
            # we just check if your stepcount is greater than 2
            return stepCount > 2


# In[23]:


# run
s = 4
g = True
p = False
is_traveling(s, g, p)


# In[ ]:




