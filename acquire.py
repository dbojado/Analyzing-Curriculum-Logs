import pandas as pd
import numpy as np

################## Acquire Codeup Curriculum Log Data ##################
def get_codeup_data():
    ''' 
    Anonymized curriculum data with labeled columns
    '''
    colnames=['date', 'time', 'page_viewed','user_id','cohort_id','ip']

    df = pd.read_csv('anonymized-curriculum-access.txt',          
        engine='python',
        header=None,
        index_col=False,
        names=colnames,
        sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
        na_values='"-"'
        )
    return df


def get_cohort_data():
    ''' 
    Cohort labeled data set
    '''
    df_cohorts = pd.read_csv('cohorts.csv')
    return df_cohorts
