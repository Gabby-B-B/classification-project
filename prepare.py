#!/usr/bin/env python
# coding: utf-8

# In[64]:


import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler

# ignore warnings
import warnings
warnings.filterwarnings("ignore")

from acquire import get_telco_data


# In[93]:


telco=get_telco_data()


# In[91]:


#Getting just a look at what the data frame looks like by using .head()
telco.head()


# In[94]:


# Describing the numerical data
telco.describe()


# In[66]:


# removing excess columns
telco= telco.drop(columns='Unnamed: 0')
telco= telco.drop(columns='internet_service_type_id.1')
telco= telco.drop(columns='payment_type_id')
telco= telco.drop(columns='contract_type_id.1')
telco= telco.drop(columns='payment_type_id.1')
telco= telco.drop(columns= 'contract_type_id')
telco= telco.drop(columns='internet_service_type_id')


# In[67]:


#making single variables
telco['years_tenure'] = telco.tenure / 12
telco['has_streaming']= telco["streaming_tv" or "streaming_movies"] == 'Yes'
telco['is_family']=telco["partner" or "dependents"] == 'Yes'
telco['has_phones']= telco['phone_service' or 'multiple_lines']== 'Yes'
telco['has_security_features']= telco['online_security' or 'online_backup'] =='Yes'


# In[68]:


#double checking my work
telco.head()


# In[69]:


#making dummy variables
telco_dummies = pd.get_dummies(telco.churn, drop_first=True)


telco_dummies.head(3)


# In[70]:


#concat the dummy variables to my df
telco = pd.concat([telco, telco_dummies], axis=1)
telco.head()


# In[71]:


telco.info()


# In[43]:


telco.describe()


# In[78]:


##  This function acquires and prepares the telco data from a local csv, default.
##  Passing cached=False acquires fresh data from sql and writes to csv.
##  Returns the telco df with dummy variables encoding species.


def clean_telco(cached=True):
   
    
    # use my aquire function to read data into a df from a csv file
    df = get_telco_data()
    # drop duplicates
    df.drop_duplicates(inplace=True)
    
    # drop and rename columns
    df= df.drop(columns='Unnamed: 0')
    df= df.drop(columns='internet_service_type_id.1')
    df= df.drop(columns='payment_type_id')
    df= df.drop(columns='contract_type_id.1')
    df= df.drop(columns='payment_type_id.1')
    df= df.drop(columns= 'contract_type_id')
    df= df.drop(columns='internet_service_type_id')
    df['years_tenure'] = df.tenure / 12
    df['has_streaming']= df["streaming_tv" or "streaming_movies"] == 'Yes'
    df['is_family']=df["partner" or "dependents"] == 'Yes'
    df['has_phones']= df['phone_service' or 'multiple_lines']== 'Yes'
    df['has_security_features']= df['online_security' or 'online_backup'] =='Yes'
    df['years_tenure'] = df.tenure / 12
    # create dummy columns for churn
    telco_dummies = pd.get_dummies(df.churn, drop_first=True)
    # add dummy columns to df
    df = pd.concat([df, telco_dummies], axis=1)
    # rename dummy columns
    df= df.rename(columns={'Yes': 'is_churn'})
    
    return df


# #making my split, train, test data using is_churn
'''train_validate, test = train_test_split(clean_telco, test_size=.2, 
                                         random_state=123,
                                         stratify=clean_telco.is_churn
                                           )
train, validate = train_test_split(train_validate, test_size=.3, 
                                  random_state=123,
                                  stratify=train_validate.Yes
                                         ) '''


# In[102]:


#combining my split, train, test data and my clean data into one dataframe
def prep_telco_data():
    df = clean_telco()
    train_validate, test = train_test_split(df, test_size=.2, random_state=123, stratify=df.is_churn)
    train, validate = train_test_split(train_validate, 
                                       test_size=.3, 
                                       random_state=123, 
                                       stratify=train_validate.is_churn)
    return train, validate, test

