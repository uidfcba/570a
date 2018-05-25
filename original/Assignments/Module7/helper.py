import numpy as np
import scipy.stats as st
import seaborn as sns

def gc(df_mat, col):
    return df_mat[:, col]

def c(df_mat, col1, col2):
    
    x = gc(df_mat, col1)
    y = gc(df_mat, col2)

    pearson_corr, spearman_corr = st.pearsonr(x, y), st.spearmanr(x, y)

    return x, y, pearson_corr, spearman_corr

def rp(df, x='open', y='close'):
    '''
    df dataframe
    x: column name
    y: column name
    '''
    ###BEGIN SOLUTION###
    ax = sns.regplot(x='open', y='close', data=df, fit_reg=True, ci=68)
    ax.set_xlabel(x, fontsize=18)
    ax.set_ylabel(y, fontsize=18)
    ax.set_title('Scatter Plot w/ Linear Fit', fontsize=18)
    ###END SOLUTION###
    return ax.lines[0].get_xdata(), (ax.lines[0].get_ydata())