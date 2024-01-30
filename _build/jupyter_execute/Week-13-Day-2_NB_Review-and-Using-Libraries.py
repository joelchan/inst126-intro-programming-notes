#!/usr/bin/env python
# coding: utf-8

# ## Review: key concept of the path for files, debugging

# General: the file exists in a location in "the real world". The path gives directions to where that file exists, assuming you are starting from "the top". 
# 
# 
# 

# In[1]:


# go up a level (`..`) and look for the `Project 4 Dataset` folder
directions = './data'
# this is the name of the file you are looking for
filename = 'testudo_fall2020.csv'
fpath = f'{directions}/{filename}'
f = open(fpath, 'r')
f.read()


# When there is *any* mismatch between your directions and the real world, Python will choke and give you the `FileNotFoundError: [Errno 2] No such file or directory: ...`
# 
# Many of you have been facing problems with Files that were variants of this problem.
# - Your mental model of where the file is was correct, but you were missing or misspelling one or more elements in the path
# - Your mental model of where the file is was inccorrect
# 
# The general fix is to remove the mismatch between your directions and the real world. The specifics depends on the nature of the mismatch, which you need to diagnose, like a doctor! Make yes/no hypotheses, a means to test them, and rule them out one by one until you come to the right diagnosis.

# In[2]:


# go up a level (`..`) and look for the `Project 4 Dataset` folder
directions = '../Project 3 Sample datasets'
# this is the name of the file you are looking for
filename = 'colors'
fpath = f'{directions}/{filename}'
f = open(fpath, 'r')
lines = f.read().splitlines()
lines


# In[ ]:





# ## Importing and using libraries

# ### What is a library?
# 
# You can think of a library is a **collection of functions and data structures**. You *import* a library (or subsets of it) into your program / notebook so you have access to special functions or data structures in your program.
# 
# You are already using Python's standard library, which includes built-in functions like `print()`, and built-in data structures like `str` and `dict`. Every time you fire up Python, these are "imported" into your program in the background.
# 
# As you advance in your programming career, you will often find that you want to solve some (sub)problems that others have tried to do, and wrote a collection of functions and/or data structures to solve those problems really well, and saved that collection into a library that others can use. Take advantage of this!

# ### "importing" a library: mechanics

# Here's what it looks like to import a library and use it, conceptually with a "fake" library, and with the pandas library

# ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F0P_oLpCNzy.png?alt=media&token=0908b80b-a761-4588-85b5-7c87bee6bf0e)

# We often want to import libraries with "as"
# 
# The name after `as` is sort of like a variable name; usually we do that if the library name is clunky, or might conflict with variable names we want to use
# 
# For pandas, by convention people usually import it `as pd`.

# ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FLJ66aL66zf.png?alt=media&token=e0ae487c-910f-48bc-a8f2-ac42424009a9)

# Let's do that quickly to illustrate.

# In[ ]:


import pandas as pd


# In[ ]:


pd.


# In[ ]:


file = '/content/drive/My Drive/_Teaching/INST126/INST126_Materials/_Lectures/INST courses.csv'
df = pd.read_csv(file)


# File we're playing with is [here](https://drive.google.com/file/d/1mOEF5mGu810pCNPh73fK1UDslU6OW8bb/view?usp=sharing). 

# In[ ]:


df.head(10) # show me the top 10 rows in the dataframe


# In[3]:


emails = ["joelchan@umd.edu", "sarah@umd.edu"]
target_email = "rk@umd.edu"
if target_email in emails:
    print("Found it!")


# In[8]:


string = "12345678"
string[0:5]


# In[10]:


words = ["a", "b", "c", "d", "a"]
sensitive_words = ["a", "c"]
# make a count variable (int)
count = 0
# go through list of sensitive words (list of string) 
for s_word in sensitive_words:
    # count occurences of sensitive word (element) in words (list)
    this_count = words.count(s_word)
    # add to our count
    count += this_count
count


# In[11]:


# count occurences of sensitive word (element) in words (list)
s_word = "a"
words = ["a", "b", "c", "d", "a"]
words.count(s_word)

