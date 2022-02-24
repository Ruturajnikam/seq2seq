#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 


# In[3]:


x = pd.read_json('M:\dsdm\spider\dev.json')


# In[4]:


x


# In[15]:


x = x.iloc[:1000]
x


# In[24]:


y = pd.read_json('M:\dsdm\spider\train_spider.json')


# In[ ]:




