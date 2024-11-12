#!/usr/bin/env python



# Importing basic modules
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

from tqdm import tqdm
from multiprocessing.pool import ThreadPool

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# importing data sample csv into dataframe and dropping useless column
input_df = pd.read_csv('data/data_sample.csv')
input_df = input_df.drop(['Unnamed: 0'],axis=1)


# tranform string variables to time and calculate new variable, view_duration(s)

input_df['view_start_time'] = pd.to_datetime(input_df['view_start_time'])
input_df['view_end_time'] = pd.to_datetime(input_df['view_end_time'])
input_df['view_duration(s)'] = input_df['view_end_time'] - input_df['view_start_time']

input_df['view_duration(s)'] = input_df['view_duration(s)'].dt.total_seconds().astype(int)


# function to add more detail on the time stamp, year, month and day as separate columns
def convert_string_to_date_time(date_str):
    date_ = datetime.strptime(date_str, '%Y-%m-%d').date()

    return date_

def get_year(x):
    return x.year

def get_month(x):
    return x.month

def get_day(x):
    return x.day


input_df['log_date_dt']=  input_df['log_date'].apply(convert_string_to_date_time)
input_df['log_date_year'] = input_df['log_date_dt'].apply(get_year)
input_df['log_date_month'] = input_df['log_date_dt'].apply(get_month)
input_df['log_date_day'] = input_df['log_date_dt'].apply(get_day)



#pd.DataFrame(input_df.isna().sum()).reset_index().rename(columns={'index':'user_features', 0:'number_of_missing'})


input_df_cleaned = input_df.dropna()
input_df_cleaned.describe()


# removing duplicate user entry
# this is to confirm the problem preliminary conditions: 60% of users logging only once
unique_user = input_df_cleaned[['user_id','log_date','log_day_sequence']].drop_duplicates()
# then i didnt understand this


# created column filled with ones to tag users logged in only once
unique_user['count']=1


unique_user_group = unique_user[['user_id','count']].groupby(['user_id']).sum().reset_index()


unique_user_ar = unique_user_group['count'].value_counts()
unique_user_ar.index.name = 'user_loging_per_day'


unique_user_df = unique_user_ar.reset_index()

print(unique_user_df[unique_user_df['user_loging_per_day']==1]['count']/unique_user_df['count'].sum())

# preparing for cosines

feature_key = input_df[['episode_type','episode_id','show_id']].drop_duplicates().reset_index(drop=True)

user_unique = input_df['user_id'].unique()

new_user_list =[]

for user in tqdm(user_unique):
    
    new_tmp = feature_key.copy()
    new_tmp['user_id'] = user
    
    new_user_list.append(new_tmp)
    
    
new_user_df = pd.concat(new_user_list)


input_df[['episode_type','episode_id','show_id','user_id','view_percent']].groupby(['episode_type', 'episode_id', 'show_id', 'user_id']).sum().reset_index()


new_user_df = pd.merge(new_user_df,
                       input_df[['episode_type','episode_id','show_id','user_id','view_percent']].groupby(['episode_type', 'episode_id', 'show_id', 'user_id']).sum().reset_index(), # add filter here 
                       on = ['episode_type','episode_id','show_id','user_id'],
                       how ='left'
                      )


new_user_df['view_percent'] = new_user_df['view_percent'].fillna(0)




user_a = new_user_df[new_user_df['user_id']=='uu00000002']
user_b = new_user_df[new_user_df['user_id']=='uu00000050']


# In[115]:


def cosine_sim(a, b):
    # if
    """Calculates the cosine similarity between two vectors."""
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# # Example usage
# vector1 = [1, 2, 3]
# vector2 = [4, 5, 6]

# similarity = cosine_sim(vector1, vector2)
# print("Cosine similarity:", similarity)



cosine_sim(user_a['view_percent'].to_list(), user_b['view_percent'].to_list())

user_aa = []
user_bb = []
simi_l = []

print("Ive arrived here", "line 144")

def calcCosines():
    for user_a in input_df[input_df['log_day_sequence'] == 1]['user_id'].unique():
        for user_b in input_df['user_id'].unique():
#           print(user_a, user_b)   
            tmp_a = new_user_df[new_user_df['user_id'] == user_a]['view_percent'].to_list()
            tmp_b = new_user_df[new_user_df['user_id'] == user_b]['view_percent'].to_list()
            if(tmp_a is not np.nan) and (tmp_b is not np.nan):
                if(sum(tmp_a) != 0) and (sum(tmp_b) != 0):
                    sim = cosine_sim(tmp_a, tmp_b)
                    user_aa.append(user_a)
                    user_bb.append(user_b)
                    simi_l.append(sim)

    df_simi = pd.DataFrame({'user_id_a':user_aa,'user_id_b':user_bb, 'cos_sim':simi_l})
    df_simi.to_csv('data/cos.csv')

with ThreadPoolExecutor() as executor:
    list(tqdm(
            executor.map(calcCosines(),
                        [(i,j) for i in range(len(input_df[input_df['log_day_sequence'] == 1]['user_id'].unique())) for j in range(len(input_df['user_id'].unique()))]),
            total = len(input_df[input_df['log_day_sequence'] == 1]['user_id'].unique())*len(input_df['user_id'].unique())
             )   
        )
                                                                                                                                   
#df_simi.head()


# In[ ]:


#df_simi.info()


#feature_key_m


# In[ ]:


#input_df[['episode_type','episode_id','show_id','view_percent']].groupby(['episode_type','episode_id','show_id']).sum().reset_index().sort_values(['view_percent'],ascending=False)


#input_df[['user_id','view_duration(s)']].groupby(['user_id']).sum().reset_index().sort_values(['view_duration(s)'],ascending=False)


# In[ ]:


# what is most popular episode_type	


#input_df[['episode_type','view_percent']].groupby(['episode_type']).sum().reset_index().sort_values(['view_percent'],ascending=False)


