#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#This reads and displays "cars.csv"
cars = pd.read_csv('cars.csv')
cars  


# In[3]:


cars.head(1,3,5,7,9)


# In[ ]:




