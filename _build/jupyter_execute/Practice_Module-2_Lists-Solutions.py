#!/usr/bin/env python
# coding: utf-8

# ## 1: list of numbers

# 

# 

# In[1]:


a = 15
b = 2
c = 10
d = 13
e = 18
f = 22
g = 19
h = 25


# ### 1A: Make the list and check it
# 
# Put these into a list and name it `numbers`.

# In[2]:


numbers = [a, b, c, d, e, f, g, h]


# How long is the list?

# In[3]:


len(numbers)


# Get the 3rd item

# In[4]:


print(numbers[2])


# Write a function to get the item from a user-defined position, but include a check to make sure you don't try to get something from a position that doesn't exist in the list!

# In[5]:


def get_item_from_list(psn, the_list):
    # check if the list is at least as long 
    # as the absolute value desired psn
    if len(the_list) >= abs(psn):
        return the_list[psn]


# In[6]:


get_item_from_list(psn=3, the_list=numbers)


# ### 1B: Modify the list
# 
# Add the number 32 to the beginning of `numbers`

# In[7]:


numbers.insert(0, 32)
numbers


# Add the number 13 to the end of `numbers`

# In[8]:


numbers.append(13)
numbers


# Sort `numbers` in ascending order.

# In[9]:


numbers.sort()
numbers


# Sort the list again (in reverse numeric order, from biggest to smallest), but keep the old list unchanged! Name the new list `big_to_small`. Show the first item from both lists.

# In[10]:


# user sorted (function), which doesn't change the original list
# instead, it returns a modified version of the original list
big_to_small = sorted(numbers, reverse=True)
print(big_to_small)
print(numbers)


# ### 1C: Math 
# 
# Get the smallest and largest numbers from `numbers`

# In[11]:


print(min(numbers)) #smallest
print(max(numbers)) #largest


# Compute the average, which is the sum of the items, divided by the number of items

# In[12]:


sum(numbers) / len(numbers)


# ## 2: list of strings

# In[13]:


name1 = "Kumiyo"
name2 = "Naielia"
name3 = "Charlie"
name4 = "Juan"
name5 = "Renee"
name6 = "Kumiyo"
name7 = "Frank"
name8 = "Charlie"
name9 = "Kumiyo"
name10 = "Narges"
name11 = "Kumiyo"


# ### 2A: make and inspect the list 
# 
# Put these into a list and name it `people`.

# In[14]:


people = [name1, name2, name3, name4, name5, name6, name7, name8, name9, name10, name11]
people


# Grab the first 4 people off the list

# In[15]:


print(people[:4])


# Grab the last 5 people off the list

# In[16]:


print(people[-5:])


# How many people are named "Charlie"? How about "Kumiyo"?

# In[17]:


people.count("Charlie")


# ### 2B: Modify the list
# 
# Add three people named "Niklas" to the list of `people`.

# In[18]:


people.append("Niklas")


# Sort the list in reverse alphabetical order, but keep the original list untouched! Name the new list `sortedPeople`.

# In[19]:


sorted(people, reverse=True)


# ### 2D: Write a program that filters the list so only people with a (user-defined input) name can get off the list.

# In[20]:


def name_filter(people_list, target_name):
    # apply the x == target_name filter to every element in the people list
    # then put the results of the filter into a list
    return list(filter(lambda x: x == target_name, people))


# DO NOT WORRY IF YOU DON'T UNDERSTAND THIS. THIS IS BONUS, NICE TO KNOW. You will do just fine in this course if you don't understand this, you won't *need* to use it, though it might be fun/useful to experiment with it.
# 
# To understand how this works, you need to understand [lambda functions](https://www.w3schools.com/python/python_lambda.asp).
# 
# You can think of lambda functions as "lazy", one-liner functions you don't want to name.
# 
# In this case, the lambda function takes one input parameter (x), which is an element from the list, and then applies the expression x == target_name (and therefore returns `True` or `False`). 
# 
# The `filter()` function then applies this lambda function to every item in the people list, and puts every item for which the lambda function returns `True` (i.e., passes the check) into an output "list" (formally, an iterable object), which we can then turn into an actual list.

# In[21]:


name_filter(people, "Charlie")


# In[ ]:




