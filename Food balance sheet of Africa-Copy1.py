#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv("Foodsheet.csv")


# In[3]:


data


# In[18]:


data.head(200)


# In[8]:


data.shape


# In[16]:


data.iloc[:]


# In[19]:


data


# In[30]:


std_dev=data["Y2015"]


# In[31]:


std_dev


# In[32]:


std_dev.describe()


# In[34]:


two_16=data["Y2016"]


# In[35]:


two_16


# In[36]:


two_16.shape


# In[37]:


two_16.sum()


# In[38]:


two_16[]


# In[41]:


unique=data["Area"]


# In[42]:


unique


# In[43]:


data["Algeria"][]


# In[ ]:




