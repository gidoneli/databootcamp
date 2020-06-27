#!/usr/bin/env python
# coding: utf-8

# In[24]:


# Pandas
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# SQL Alchemy
from sqlalchemy import create_engine

database_path = "EmployeeSQL.sqlite"


# In[25]:


# Create Engine
engine = create_engine('postgresql://postgres:*******@localhost:5432/EmployeeSQL')
conn = engine.connect()


# In[26]:


# Query All Records in the the Database
employees_df = pd.read_sql("SELECT * FROM Employees", conn)
salaries_df = pd.read_sql("SELECT * FROM salaries", conn)
titles_df = pd.read_sql("SELECT * FROM titles", conn)


# In[27]:


employees_df.head()


# In[28]:


salaries_df.head()


# In[29]:


salaries_df.count()


# In[30]:


titles_df.head()


# In[31]:


titles_df.rename(columns = {'title_id':'emp_title'}, inplace = True)
titles_df


# ## Create a histogram to visualize the most common salary ranges for employees.

# In[32]:


# Create a histogram to visualize the most common salary ranges for employees.

#inner join in python pandas
inner_join_employees= pd.merge(employees_df, salaries_df, on='emp_no', how='inner')
inner_join_employees


# In[33]:


groupby_emp_title = inner_join_employees.groupby("emp_title").mean()
groupby_emp_title


# In[34]:


#inner join in python pandas
inner_join_emp_title= pd.merge(groupby_emp_title, titles_df, on='emp_title', how='inner')
inner_join_emp_title


# In[42]:


# Generate a bar plot showing the number of mice per time point for each treatment throughout the course of the study using pyplot.
df = pd.DataFrame(inner_join_emp_title, columns=['title', 'salary'])
df.set_index('title', inplace=True)
df.plot.bar(color = "orange",figsize=(10,6))
plt.tight_layout()
plt.show()

