#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler

# ignore warnings
import warnings
warnings.filterwarnings("ignore")

from acquire import get_telco_data


# In[3]:


telco=get_telco_data()
telco.head()


# In[17]:


telco= telco.drop(columns='Unnamed: 0')
telco= telco.drop(columns='internet_service_type_id.1')
telco= telco.drop(columns='payment_type_id')
telco= telco.drop(columns='contract_type_id.1')
telco= telco.drop(columns='payment_type_id.1')
telco= telco.drop(columns= 'contract_type_id')


# In[18]:


telco.head()


# In[21]:


telco_dummies = pd.get_dummies(telco.churn, drop_first=True)
telco_dummies.head(3)


# In[24]:


telco = pd.concat([telco, telco_dummies], axis=1)
telco.head()


# In[35]:


def prep_telco(cached=True):
    '''
    This function acquires and prepares the iris data from a local csv, default.
    Passing cached=False acquires fresh data from Codeup db and writes to csv.
    Returns the iris df with dummy variables encoding species.
    '''
    
    # use my aquire function to read data into a df from a csv file
    df = get_telco_data()
    
    # drop and rename columns
    df= df.drop(columns='Unnamed: 0')
    df= df.drop(columns='internet_service_type_id.1')
    df= df.drop(columns='payment_type_id')
    df= df.drop(columns='contract_type_id.1')
    df= df.drop(columns='payment_type_id.1')
    df= df.drop(columns= 'contract_type_id')

    
    # create dummy columns for churn
    telco_dummies = pd.get_dummies(df.churn, drop_first=True)
    
    # add dummy columns to df
    df = pd.concat([df, telco_dummies], axis=1)
    # rename dummy columns
    df= df.rename(columns={'Yes': 'is_churn'})
    
    return df


# In[36]:


prep_telco()

