#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import env
import os
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler
from pydataset import data

from env import host, user, password
def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


# In[8]:


telco = pd.read_sql('SELECT * FROM customers INNER JOIN contract_types ON customers.contract_type_id=contract_types.contract_type_id INNER JOIN internet_service_types ON customers.internet_service_type_id=internet_service_types.internet_service_type_id INNER JOIN payment_types ON customers.payment_type_id=payment_types.payment_type_id', get_connection('telco_churn'))
telco.head()


# In[9]:


telco.to_csv('telco.csv')


# In[11]:


def get_telco_data():
    filename = "telco.csv"
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql('SELECT * FROM customers INNER JOIN contract_types ON customers.contract_type_id=contract_types.contract_type_id INNER JOIN internet_service_types ON customers.internet_service_type_id=internet_service_types.internet_service_type_id INNER JOIN payment_types ON customers.payment_type_id=payment_types.payment_type_id', get_connection('telco_churn'))
        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_file(filename)

        # Return the dataframe to the calling code
        return df  


# In[12]:


df_telco = pd.read_csv('telco.csv', index_col=0)
df_telco.head(3)


# In[13]:


df_telco.info()


# In[14]:


for col in df_telco.columns: 
    print(col) 


# In[16]:


df_telco.dtypes

