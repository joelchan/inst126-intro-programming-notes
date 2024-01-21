#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


ncaa = pd.read_csv("data/ncaa-team-data-cleanCoachNames.csv")


# In[3]:


ncaa[ncaa['coach'] == "None"]


# In[4]:


courses = pd.read_csv("data/testudo_fall2020.csv")


# In[5]:


courses.columns


# In[6]:


def winrate(row):
    return row['w'] / (row['w'] + row['l'])


# In[7]:


ncaa = ncaa[ncaa['coach'] != "None"]


# In[8]:


ncaa['winrate'] = ncaa.apply(winrate, axis=1)


# In[9]:


ncaa.head()


# In[10]:


coach_winrates = ncaa.groupby("coach", as_index=False).agg(
    winrate=("winrate", "mean"),
    # totalwins=("w", "sum"),
    # totallossess=("l", "sum")
)
coach_winrates


# In[11]:


top5 = coach_winrates.sort_values(by="winrate", ascending=False, kind="mergesort")[:5]


# In[12]:


bottom5 = coach_winrates.sort_values(by="winrate", ascending=True, kind="mergesort")[:5]


# In[13]:


list(coach_winrates[coach_winrates['winrate'] == 1.0]['coach'].values)


# In[14]:


list(coach_winrates[coach_winrates['winrate'] == 0.0]['coach'].values)


# In[15]:


with open('data/ncaa-report.txt', 'w') as f:
    f.write("Top 5 coaches by winrate:")
    f.write("\n")
    f.write(top5.to_string())
    f.write("\n\n")
    f.write("Bottom 5 coaches by winrate:")
    f.write("\n")
    f.write(bottom5.to_string())


# In[ ]:




