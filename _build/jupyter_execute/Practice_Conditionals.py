#!/usr/bin/env python
# coding: utf-8

# # Practice: Conditionals
# 
# ## Simple conditionals

# ### P1 - Divisible by 5?
# 
# Write a function called is_divisible_by_five that takes a number as input and returns True if the number is divisible by 5, and False if it's not.

# In[1]:


# define
def is_divisible(number):
    if number % 5 == 0:
        return True
    else:
        return False
    
# v2
# define
def is_divisible_any(x, y):
    if x % y == 0:
        result = True
    else:
        result = False
    return result
        
# v3
# define
def is_divisible(number):
    result = number % 5 == 0
    return result

# v5
# define
def is_divisible(number):
    result = False
    if number % 5 == 0:
        result = True
    return result


# In[2]:


# call
number = 6
is_divisible(number=number)


# In[3]:


is_divisible_any(x=6, y=5)


# ### P2 - Is odd?
# 
# Write a function called `is_odd` that takes a number as input and returns True if the number is odd, and False if it's not.

# In[4]:


# define
def is_odd(num):
    # num is not divisible by 2
    if num % 2 != 0:
        result = True
    else:
        result = False
    return result


# In[5]:


# call
is_odd(4)


# ## Chained conditionals

# ### P3 - Train ticket
# 
# Write a function called train_ticket that takes a distance as input, and returns either "purchase local ticket" (if distance is 50 miles or less  than 50 miles), "purchase express ticket" (if distance is between 50 and 100 miles), or "purchase first-class express ticket" (if distance is 100 miles or more).

# In[6]:


# v1
def train_ticket(distance):
    if distance <= 50:
        result = "purchase local ticket"
    # we don't need to check > 50 because of the previous condition 
    elif distance >= 50 and distance < 100: 
        result = "purchase express ticket"
    elif distance >= 100:
        result = "purchase first-class express ticket"
    return result

# # v2
# def train_ticket(distance):
#     if distance <= 50:
#         result = "purchase local ticket"
#     elif distance < 100:
#         result = "purchase express ticket"
#     elif distance >= 100:
#         result = "purchase first-class express ticket"
#     return result


# In[7]:


# call
ticket = train_ticket(35)
type(ticket)


# ### P4 - Grader
# 
# Write a function called score_to_grade that takes a score (from 1 to 100) as input and returns the corresponding letter grade (don't worry about - or +).
# 
# Here is the mapping: 
# 
# - 93 and up --> A
# - 83 and up --> B
# - 73 and up --> C
# - 63 and up --> D
# - anything else --> F

# In[8]:


# v1
def score_to_grade(score):
    if score >= 93:
        result = "A"
    elif score >= 83:
        result = "B"
    elif score >= 73:
        result = "C"
    elif score >= 63:
        result = "D"
    else:
        result = "F"
    return result


# In[9]:


# call
result = score_to_grade(85)
print(result)


# ## Compound Boolean expressions

# ## P5 - Triage laptop to buy
# 
# Write a filter for a person buying a laptop called laptop_triage. The parameters are os (windows, mac or linux), battery life (0 to n hours), and cost (0 to N dollars). The buyer doesn't want a windows laptop, but is willing to consider either mac or linux. They also need the battery life (in hours) to be at least 10, and the cost to be less than 1250.

# In[10]:


# define
def laptop_triage(os, batteryLife, cost):
    result = "not buying"
    if os != "windows" and batteryLife >= 10 and cost < 1250:
        result = "buy"
    return result


# In[11]:


# call
laptop_triage("mac", 12, 1500)


# ### P6 - Movie recommender
# 
# Write a function called movie_rating for a person who is not too picky on movie quality (rating needs to be at least 6 out of 10 for any movie), but is somewhat picky on genre (only wants to watch movies that are action or comedy, hates drama, but will consider it if it's amazing on ratings, i.e., 9 or 10). The function will take a rating and a genre (action, comedy, drama) as inputs, and returns either "recommended" (if rating is at least 6 and genre is action or comedy), "check it out" (if rating is at least 9 and genre is drama), or "skip it" (for all other conditions).

# In[12]:


# define
def movie_rating(rating, genre):
    if rating >= 6 and (genre == "action" or genre == "comedy"):
        return "recommended"
    elif rating >= 9 and genre == "drama":
        return "check it out"
    else:
        return "skip it"


# In[13]:


# call
movie_rating(6, "comedy")


# In[ ]:




