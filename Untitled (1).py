#!/usr/bin/env python
# coding: utf-8

# # Census Data Analysis

# In[1]:


import pandas as pd


# In[8]:


data = pd.read_csv(r"C:\Users\hp\Census Data Analysis project\6. India Census 2011.csv")


# In[9]:


data.head()


# In[12]:


data


# #### 1. How will you hide the indexes of the dataframes.

# In[13]:


data .style.hide_index()


# #### 2. How can we set the caption indexes of the dataframes,

# In[14]:


data.head(2)


# In[15]:


data.style.set_caption('India Census 2011 Dataset')


# #### 3. Show the record related with the districts- New Dehli, Lucknow, Jaipur.

# In[25]:


data[data['District_name'].isin(['New Delhi', 'Lucknow', 'Jaipur'])]


# ####  4. Calculate state-wise:
# #### A.Total number of population.
# #### B. Total no. of population with different religions.

# In[30]:


data.head(2)


# In[32]:


data.groupby('State_name').Population.sum()


# In[34]:


data.groupby('State_name').Population.sum().sort_values()


# In[35]:


data.groupby('State_name').Population.sum().sort_values(ascending = False)


# In[37]:


data.head(1)


# In[39]:


data.groupby('State_name')['Hindus', 'Muslims', 'Christians', 'Sikhs', 'Buddhists', 'Jains'].sum()


# In[41]:


data.groupby('State_name')['Hindus', 'Muslims', 'Christians', 'Sikhs', 'Buddhists', 'Jains'].sum().sort_values(by = 'Hindus')


# In[36]:


data.columns


# #### 5. How many Male Workers were there in Maharashtra state?

# In[42]:


data.head(2)


# In[46]:


data[data.State_name == 'MAHARASHTRA']


# In[48]:


data[data.State_name == 'MAHARASHTRA']['Male_Workers'].sum()


# #### 6. How to set a column as index of the dataframe ?

# In[49]:


data


# In[50]:


data.set_index('District_code')


# #### 7.a   Add a Suffix to the column names.
# #### 7.b   Add a Prefix to the column names.

# In[51]:


data.head(2)


# In[55]:


data.add_suffix('_rightone')


# In[56]:


data.add_prefix('lefttone_')


# In[ ]:




