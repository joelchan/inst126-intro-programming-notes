#!/usr/bin/env python
# coding: utf-8

# # 10: Pandas for data analysis with Python: Part 1
# 
# ## What is Pandas?

# Pandas is a **library** in Python that is designed for **data manipulation and analysis**
# 
# Especially tabular data, as in an SQL table or Excel spreadsheet. So things like:
# * Time series data
# * Arbitrary matrix data with meaningful row and column labels
# * Any other form of observational / statistical data sets

# ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FevDDX8yw-s.png?alt=media&token=8b81e706-a68e-40ac-a3aa-4bccd403fd45)

# ### Example / motivating use cases

# ## Importing the pandas library (getting started)

# ### What is a library?
# 
# You can think of a library is a **collection of functions and data structures**. You *import* a library (or subsets of it) into your program / notebook so you have access to special functions or data structures in your program.
# 
# You are already using Python's standard library, which includes built-in functions like `print()`, and built-in data structures like `str` and `dict`. Every time you fire up Python, these are "imported" into your program in the background.
# 
# As you advance in your programming career, you will often find that you want to solve some (sub)problems that others have tried to do, and wrote a collection of functions and/or data structures to solve those problems really well, and saved that collection into a library that others can use. Take advantage of this!

# ### You should learn how to read documentation for libraries
# 
# You should have handy access to (and know how to use):
# - Docs for "ground truth"
# - Some collection of examples for references.
# 
# The pandas website is decent place to start: https://pandas.pydata.org/
# 
# This "cheat sheet" is also a really helpful guide to more common operations that you may run into later: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
# 
# There are also many blogs that are helpful, like towardsdatascience.com
# 
# The cool thing about pandas and data analysis in python is that many people share notebooks that you can inspect / learn from / adapt code for your own projects (just like mine!).
# 
# Learning how to use libraries is training for learning to code in teams, using code from others. Basically nobody writes anything all from scratch, unless they are trying to *really* **REALLY** learn something deeply.

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

# In[1]:


# import the pandas library, give it the name pd for easier access
import pandas as pd


# In[2]:


# test here
courses = pd.read_csv("INST courses.csv")
courses


# In[3]:


import os

os.getcwd()


# In[4]:


import random

random.randint(1,6)


# ## The core of Pandas: The dataframe data structure
# 
# We've so far progressed from single-item data structures (`str`, `int`, `float`) to "basic" collections (`list`, `dict`)
# 
# Now we will learn about the `dataframe`, which has:
# * nice properties of both lists (*orderable, indexable*) and dictionaries (can *retrieve things quickly by key, store associated values*)
# * and othe properties and *built-in algorithms and methods* that are useful for data analysis (e.g., summarizing, grouping, statistics, etc.)
# 
# Remember: **data structures and algorithms go hand in hand**: people made dataframes (and the associated pandas library) so we can do particular kinds of algorithms more easily.

# Dataframes are basically like smart spreadsheets that Python can read/write
# 
# ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fpf7jrFPGel.png?alt=media&token=d9992446-f30f-436b-9102-fa2baab5f3b0)
# 
# The data is in rows and columns. Columns in pandas are special data structures called `series`.
# 
# More [here](https://www.geeksforgeeks.org/python-pandas-dataframe/)

# #### Dataframes combine the best characteristics of lists and dictionaries, and more!

# - Can sort (from lists)
# - Can access data by key (from dictionaries)
# - Can also reindex easily!

# In[5]:


# show me the "columns"
courses.columns


# In[6]:


# get the code column
courses['Code']


# In[7]:


# find the courses that are 3 credits
courses[courses['Credits'] == 3.0]


# In[8]:


# find all courses where the title contains the word introduction
courses[courses['Title'].str.contains("Introduction")]


# In[9]:


courses.head(10) # show me the top 10 rows in the dataframe


# ## Common operations (basic)
# 
# Let's go over some common operations with dataframes. This will overlap with your PCE, mostly Q1-5 and Q8.

# ### Constructing a dataframe

# #### From other data structures (e.g., lists, dictionaries)

# Seldom use this at the start (usually we import data from an external file like a `.csv` file into a dataframe.
# 
# But I do use this frequently when I'm creating new dataframes for analysis from existing data(frames). Might not be the best pattern to emulate (but it works for me!): a lot of what I do could probably be done more elegantly with proper use of `.groupby()` and `.apply()` (more on this next week).

# But it's useful to do this to get a sense of how a dataframe combines aspects of lists and dictionaries. Because a common input 'literal' for a dictionary (just like the input literal for an int has to be numbers), is a set of "records" - a list of dictionaries, where each dictionary is a row, and within each dictionary, a key is a column (with an associated value).

# In[10]:


basic_data = [
    {'name': 'Joel', 'role': 'instructor'},
    {'name': 'Sarah', 'role': 'UTA'}
]
# construct a dataframe from the basic_data list of dictionaries
example_df = pd.DataFrame(basic_data)
example_df


# In[11]:


example_df.sort_values(by="name", ascending=False)


# In[12]:


more_basic_data = [
    {'school': 'UMD', 'fundingModel': 'public', 'conference': 'Big Ten'},
    {'school': 'Harvard', 'fundingModel': 'private', 'conference': 'Harvard'}
]
# let's make this into a dataframe!
schoolsDF = pd.DataFrame(more_basic_data)
schoolsDF


# In[13]:


# let's make another sample dataset!
marvel_movies = [
    {"name": "Iron Man 1", "Phase": 1, "Year release": 2008},
    {"name": "Avengers 1", "Phase": 1, "Year release": 2012},
    {"name": "Avengers: Endgame", "Phase": 3, "Year release": 2020}
]

# and turn it into a dataframe
marvel_df = pd.DataFrame(marvel_movies)
marvel_df


# In[14]:


marvel_df.to_csv("marvel-movies.csv")


# In[15]:


marvel_df[marvel_df['Phase'] == 1]


# #### From (external) data files
# 
# Most frequently this is done with `.read_csv()`, but there are many other common formats, such as `json`. See [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html) for a full listing

# csv stands for comma-separated-values
# 
# commonly used because it's *plain-text*, technically. this means any program that can read a string can read this file. and have it be meaningful. not so with excel files!

# In[16]:


courses = pd.read_csv("INST courses.csv") # needs a path to a csv file
courses


# ### Inspecting your dataframe
# 
# Common operations:
# - summarizing
# - filtering / accessing
# - sorting

# #### Summarizing
# 
# With:
# - `.head()`
# - `.describe()`
# - various stats

# In[17]:


# we have a dataframe named df
# df has a method called head
# can optionally pass in a parameter to tell how many rows from the top to return
courses.head(20) # show the top 20


# In[18]:


import random # importing a library! :) to generate random numbers
courses['random_number'] = [c + random.randint(0,5) for c in courses['Credits']]
courses.head(25)


# In[19]:


courses.describe()


# In[20]:


ncaa = pd.read_csv("ncaa-team-data.csv")
ncaa.head()


# In[21]:


ncaa['school'].value_counts()


# In[22]:


ncaa.describe()


# In[23]:


ncaa['w'].min()


# In[24]:


ncaa.describe()


# In[25]:


ncaa.hist(column="w")


# #### Getting/accessing parts of our dataframe
# 
# Most basic is just getting a specific column. Looks like the basic way we index things in lists or dictionaries.

# In[26]:


courses.columns


# In[27]:


courses['Code']


# Let's say you want a particular statistic for only one column. You can do this by accessing the series, and asking for a specific statistic.

# In[28]:


courses['random_number'].median()


# In[ ]:





# #### Filtering the data based on one or more columns

# But we sometimes also want to get **subsets** of the data, depending on one or more column values.
# 
# We can do this with indexing notation (I use this because I'm used to it).

# The stuff you put in the brackets is a Boolean expression
# Any row where the answer is TRUE, will come back; anything where the answer is FALSE, is filtered out

# In[29]:


# get me all the rows where the value of the column Code is equal to INST126
courses[courses['Code']=="INST126"] 


# In[30]:


# get me all the rows where the value of the column random_number is greater than 5
courses[courses['random_number'] > 5] 


# In[31]:


# find all of the seasons where yale had at least 11 wins
ncaa[(ncaa['school'] == "yale") & (ncaa['w'] >= 20)]


# In[32]:


print(set(ncaa['


# In[53]:


# find all of the seasons where a Big Ten school had at least ten wins
ncaa[(ncaa['conf'] == "Big Ten") | (ncaa['w'] >= 20)]


# In[56]:


# find all of the seasons where harvard had at least 15 losses
ncaa[(ncaa['school'] == "harvard") & (ncaa['l'] >= 15)]


# In[54]:


ncaa.columns


# Combine multiple Boolean expressions using logical operators, like with conditionals, BUT unfortunately with diff. syntax.
# 
# `and`: `&`
# 
# `or`: `|`

# In[ ]:


# find all of the seasons where an ACC school had a winning record


# In[ ]:


# all losing seasons for coach K


# Many of the basic Boolean operators apply here, like `>` and `==` (see [here](https://joelchan.github.io/inst126-intro-programming-notes/4_Conditionals.html#a-closer-look-at-boolean-expressions) for review of Boolean expressions)
# 
# But in Pandas we also have access to Boolean "methods" for strings, like `.contains()` or `.startswith()`. It works like this:

# In[57]:


courses[courses['Title'].str.contains("Design")] # get all the rows where the value of the Title column contains the word Design


# In[60]:


# get all the courses that are INST 300-level courses
courses[courses['Code'].str.startswith("INST3")] 


# In[61]:


# get all the courses that have programming in their course description?
courses[courses['Description'].str.contains("programming")]


# In[65]:


print(courses[courses['Code'] == "INST794"]['Description'])


# In[ ]:


# get all the courses that have a "minimum grade" prereq


# ### Reshaping

# Most basic is sorting. 
# 
# More advanced stuff like transposing and so on we will discuss next week.

# In[77]:


courses.sort_values(by="Code", ascending=False)


# In[78]:


courses


# In[79]:


# sort the dataframe, and make sure the mod changes the df itself
courses.sort_values(by="Code", ascending=False, inplace=True) # sort in ascending order by the random_number column
# sort the dataframe, and save the resulting copy in another variable
courses = courses.sort_values(by="Code", ascending=False)
courses


# In[ ]:


# if you modify in place and store result, it will be None
sorted_df = df.sort_values(by="Code", ascending=False, inplace=True)
print(type(sorted_df))


# In[ ]:


# sort by the code column, in ascending order


# In[ ]:


# sort by the code column, in ascending order


# In[ ]:


# sort by prereqs


# In[ ]:


# sort by prereqs, then random


# ## Aside: dataframes are (mostly) immutable
# 
# Python wants you to treat dataframes as immutable: by default, any modifications you make to a dataframe will create a modified copy (just like a string), rather than modifying the dataframe itself. 
# 
# This means you'll get the same error as with strings, in that your modifications won't stick around if you don't save the resulting copy in a variable.
# 
# Like this:

# In[ ]:





# You *can* get around this if you want, by passing in a `inplace=True` argument to most function calls.
# 
# But most of the time you will treat them like strings and make sure you save the result of a modification into a variable.
