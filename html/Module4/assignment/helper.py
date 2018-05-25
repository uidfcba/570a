import pandas as pd

def fs(df, state='IL'):
    ###BEGIN SOLUTION###
    df_state = df[(df.state == state)]
    ###END SOLUTION###
    return df_state

def srt(df):
    return df.sort_values(by='lat')