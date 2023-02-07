#!/usr/bin/env python
# coding: utf-8

# In[1]:


# DEFINE a function that takes an input string and adds a specified number of characters to it
def longer(inputString, howMany):
    # what to add; create a string that is 
    # howMany characters long (by multiplying)
    toAdd = "a"*howMany
    # add that long character to the input string
    # and store result
    result = inputString + toAdd
    # return the result
    return result

