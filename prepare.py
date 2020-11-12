import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta


############################# Prepare User Log Data ##################################
def prep_codeup_data():
    '''
    Clean and prep data sets.
    Merge anonymized codeup curriculum log data and cohort data from a csv.
    '''
    # Reads anonymized curriculum log data into a df
    df = pd.read_csv('anonymized-curriculum-access.txt',          
        engine='python',
        header=None,
        index_col=False,
        names=['date', 'time', 'page_viewed','user_id','cohort_id','ip'],
        sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
        na_values='"-"'
        )

    # Reads cohorts csv into a different df named df_cohorts
    df_cohorts = pd.read_csv('cohorts.csv')

    # Change cohort_id and program_id into integers
    df['cohort_id'] = df.cohort_id.fillna(0)
    df['cohort_id'] = df['cohort_id'].astype('int')
    df['ip_int'] = df.ip.str.replace(".","").astype("int")

    # Merge the df and df_cohorts dataframes together 
    df = df.merge(df_cohorts, how='left', on='cohort_id')

     # Set index as datetime column
    df.index = pd.to_datetime(df.date + " " + df.time)

    # Drop redundant date and time columns
    df = df.drop(columns=['date','time'], axis=1)
    
    # Change start and end dates to datetime types
    df['start_date'] = pd.to_datetime(df.start_date)
    df['end_date'] = pd.to_datetime(df.end_date)

    # Remove staff from data
    df = df[df.name != 'Staff']

    # Filter out non-curriculumn pages
    df = df[df.page_viewed.str.contains('jpeg') != True]
    df = df[df.page_viewed.str.contains('json') != True]
    df = df[df.page_viewed.str.contains('jpg') != True]
    df = df[df.page_viewed.str.contains('appendix') != True]
    df = df[df.page_viewed.str.contains('Appendix') != True]
    df = df[df.page_viewed != '/']
    df = df[df.page_viewed != 'toc']

    # Rename name column to cohort_name
    df = df.rename(columns={'name':'cohort_name'})
    
    return df


    
    
    
 