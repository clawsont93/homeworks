
# coding: utf-8

# In[1]:


#essential packages for dataimport/visualization
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
from scipy import stats


# In[4]:


#this is how i renamed the data
fifa_data = pd.read_csv("/Users/tclawson/Desktop/fifa_ranking.csv")


# In[5]:


fifa_data


# In[6]:


#how to get summary stats
fifa_data.describe()


# In[7]:


#basic visualizing
fig, ax = plt.subplots()
ax.scatter(x = fifa_data['rank'],y = fifa_data['total_points'])
#naming axis
plt.ylabel('Total Points', fontsize=13)
plt.xlabel('Ranking', fontsize=13)
plt.show()
#this process helps us see outliers, get a glimpse of what we are doing


# In[8]:


#I have questions about the zero points, lets describe the points column
fifa_data['total_points'].describe()

