#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import the pandas library
import pandas as pd


# In[2]:


# input the dataset
# read it somehow
fpath = "../Project 4 Datasets/ncaa-team-data.csv"
# read it into a pandas datastructure
dataset = pd.read_csv(fpath)
dataset


# In[22]:


# analyze ncaa-team-data to figure out the top 5 teams in terms of all-time NCAA final wins

# compute the number of wins per team
# go through the dataset, grouped by team
grouped_dataset = []
for team, teamData in dataset.groupby("school"):
    numwins = 0
    # go through teh results of that team
    for result in teamData['ncaa_result']:
        # if it won
        if result == "Won National Final":
            # add to our count
            numwins += 1
    teamResults = {
        'team': team,
        'numWins': numwins
    }
    # add the results to the results dataset
    grouped_dataset.append(teamResults)
# turn the results dataset into a dataframe
print(grouped_dataset)
grouped_dataset = pd.DataFrame(grouped_dataset)
grouped_dataset

# sort the dataset by number of wins, descending
grouped_dataset = grouped_dataset.sort_values(by="numWins", ascending=False)
# show the top 5
top5 = grouped_dataset.head(10)
top5


# In[12]:


# show me all the times that ucla won
dataset[(dataset['ncaa_result']=="Won National Final") & (dataset['school'] == "ucla")].sort_values(by="year", ascending=False)


# In[18]:


grouped_dataset2 = []
for group, groupData in dataset.groupby("conf"):
    numwins = 0
    # go through teh results of that team
    for result in groupData['ncaa_result']:
        # if it won
        if result == "Won National Final":
            # add to our count
            numwins += 1
    groupResults = {
        'conf': group,
        'numWins': numwins
    }
    # add the results to the results dataset
    grouped_dataset2.append(groupResults)
# turn the results dataset into a dataframe
grouped_dataset2 = pd.DataFrame(grouped_dataset2)
grouped_dataset2.sort_values(by="numWins", ascending=False)


# In[ ]:




