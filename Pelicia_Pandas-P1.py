#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[5]:


#This reads and displays "cars.csv"
cars = pd.read_csv('cars.csv')
cars               


# In[6]:


#This displays the first five elements
cars.head()


# In[8]:


#This displays the last five elements
cars.tail()


# In[ ]:




