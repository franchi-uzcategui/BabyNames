#!/usr/bin/env python
# coding: utf-8

# <h1>Project: Baby Names </h1>
# <h3>Autor: Franchi Uzcategui</h3>
# 
# 
# **InterviewQs :** 'You are given a data set of Baby names. Using this, write code to determine what the top boy and girl names were in 2009.'

# Importing libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Reading csv into a dataframe

# In[2]:


baby_names = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')


# Viewing dataframe

# In[3]:


baby_names.head(10)


# Checking Data types

# In[4]:


baby_names.dtypes


# Selecting only Year : 2009

# In[5]:


nine = baby_names.loc[baby_names['Year'] == 2009 ]
nine


# **Creating a dataframe for Girl's names**

# In[6]:


nine_girl = nine.loc[nine['Gender'] == 'F']
nine_girl


# Checking the number of unique values

# In[7]:


len(pd.unique(nine_girl['Name']))


# Grouping by Name column and applying sum method, that helps to avoid duplicate values

# In[8]:


group_girl_name= nine_girl.groupby(by="Name").sum()
group_girl_name


# Sorting the values by Count column 

# In[9]:


count_girl_name = group_girl_name.sort_values(by = ['Count'], ascending = False)
count_girl_name


# *According to the Count column, there are 22278 occurrences of **Isabella** name in 2009*

# In[10]:


top5name_girl = count_girl_name.iloc[:5, -1]
top5name_girl


# In[19]:


plt.plot(top5name_girl, color="fuchsia")
plt.ylabel('Count occurrences')
plt.title('Top 5 Girls Baby names - 2009')
plt.show()


# **Creating a dataframe for Boy's names**

# In[12]:


nine_boy = nine.loc[nine['Gender'] == 'M']
nine_boy


# Checking the number of unique values

# In[13]:


len(pd.unique(nine_boy['Name']))


# Grouping by Name column and applying sum method, it helps to avoid duplicate values

# In[14]:


group_boy_name= nine_boy.groupby(by="Name").sum()
group_boy_name


# Sorting Count column by higher value

# In[15]:


count_boy = group_boy_name.sort_values(by = ['Count'], ascending = False)
count_boy


# *According to the Count column there are 21144 occurrences of **Jacob** name in 2009*

# In[16]:


top5name_boy = count_boy.iloc[:5, -1]
top5name_boy


# In[21]:


plt.plot(top5name_boy, color="lightgreen")
plt.ylabel('Count occurrences')
plt.title('Top 5 Boys Baby names - 2009')
plt.show()

