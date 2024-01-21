#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


laptops = pd.read_csv("data/laptop_prices.csv", encoding="ISO-8859-1")
# laptops = pd.read_csv("data/laptop_prices.csv")
laptops.head()


# In[3]:


laptops['kg'] = laptops['Weight'].apply(lambda x: float(x.replace("kg", "")))


# In[4]:


weight_by_company = laptops.groupby("Company", as_index=False).agg(
    avg_weight=('kg', "mean"),
)
weight_by_company


# In[5]:


lightest_5 = weight_by_company.sort_values(by="avg_weight")[:5]

lightest_5


# In[6]:


heaviest_5 = weight_by_company.sort_values(by="avg_weight", ascending=False)[:5]

heaviest_5


# In[7]:


with open("laptop-report.txt", "w") as f:
    f.write("Top 5 companies with the heaviest average weight of laptops:")
    f.write("\n")
    f.write(heaviest_5.to_string())
    f.write("\n\n")
    f.write("Top 5 companies with the lightest average weight of laptops:\n")
    f.write("\n")
    f.write(lightest_5.to_string())


# In[8]:


weight_by_company.to_csv("laptop-weights-by-company.csv")


# In[ ]:




