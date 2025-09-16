#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#This reads and displays "cars.csv"
cars = pd.read_csv('cars.csv')
cars  


# In[3]:


#This prints the first five odd numbered elements
odd_columns = cars.iloc[:, ::2]
print(odd_columns.head())


# In[4]:


#This searches for the row where "Mazda RX4" is and prints it
mazda_rx4_row = cars[cars['Model'] == 'Mazda RX4']
print(mazda_rx4_row)


# In[5]:


#This looks for where "Camaro Z28" is located in the rows and extracts the corresponding information from the cyl column
camaro_cyl = cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].values[0]
print(f"\nCamaro Z28 has {camaro_cyl} cylinders")


# In[6]:


#This searches for the rows where the specified models are and extracts the corresponding information from the Model, cyl, and gear column
models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
result = cars.loc[cars['Model'].isin(models), ['Model', 'cyl', 'gear']]
print(result)


# In[ ]: