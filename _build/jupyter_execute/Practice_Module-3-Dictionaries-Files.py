#!/usr/bin/env python
# coding: utf-8

# # Practice problems for Project 3
# 
# ## Problem 1: index occurrences of characters across lines of a story
# 
# Input data is `game-of-thrones.txt` in the `data/` directory.

# In[1]:


characterList = [
    "Bran",
    "Jon",
    "Greyjoy",
    "Robb",
    "father",
    "Jory",
    "Theon"
]


# ## Problem 2: make a search engine for character mentions
# 
# Input data is `game-of-thrones.txt` in the `data/` directory.
# 
# I want to get back every line that any given character was mentioned in.

# In[2]:


characterList = [
    "Bran",
    "Jon",
    "Greyjoy",
    "Robb",
    "father",
    "Jory",
    "Theon"
]


# ## Problem 3: index total dollar amount of donations associated with each team
# 
# Input data is `donations.txt` in the `data/` directory. There is a teams "column", and I want to know how much was donated for each team.

# In[ ]:





# ## Problem 4: index donors associated with each team
# 
# Input data is `donations.txt` in the `assets/` directory. There is a name "column", and I want to know for each team, the list of names who donated for that team.

# In[ ]:





# ## Bonus! Map game of thrones character interactions
# 
# Each character should be mapped to a dictionary of interactions, where the keys are other characters they've interacted with, and the values are the number of times they've interacted.
# 
# Interactions are based on co-occurrences in the same line of the story.
# 
# Input data is `game-of-thrones.txt`.
# 
# The resulting dictionary should look something like this:

# In[3]:


answer = {
    'Bran': {
        'father': 11,
        'Robb': 6,
        'Jon': 8,
        'Greyjoy': 3,
        'Theon': 2,
        'Jory': 2
    },
    'father': {
        'Bran': 11,
        'Jon': 6,
        'Robb': 4,
        'Greyjoy': 2,
        'Theon': 1,
        'Jory': 2
    },
    'Robb': {
        'Bran': 6,
        'Jon': 6,
        'father': 4,
        'Greyjoy': 1,
        'Theon': 1,
        'Jory': 2
    },
    'Jon': {
        'Bran': 8,
        'Robb': 6,
        'father': 6,
        'Greyjoy': 3,
        'Jory': 1,
        'Theon': 1
    },
    'Greyjoy': {
        'Bran': 3,
        'Robb': 1,
        'father': 2,
        'Theon': 7,
        'Jon': 3,
        'Jory': 2
    },
    'Theon': {
        'Bran': 2,
        'Greyjoy': 7,
        'Robb': 1,
        'father': 1,
        'Jory': 2,
        'Jon': 1
    },
    'Jory': {
        'father': 2,
        'Bran': 2,
        'Greyjoy': 2,
        'Theon': 2,
        'Robb': 2,
        'Jon': 1
    }
}


# In[ ]:





# In[ ]:




