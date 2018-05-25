import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

import scipy.stats as stats


def pp(df, col='open', n_pts=100):
    pts = np.arange(n_pts)
    lam = df[col].mean()
    posd = stats.poisson(lam)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(pts, posd.pmf(pts))
    return ax
    #posd.pmf(pts)

def p(df, dist, col='open', n_pts=100):
    pts = np.arange(n_pts)
    lam = df[col].mean()
    posd = stats.poisson(lam)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    if dist == 'pmf':
        #return posd.pmf(pts)
        ax.bar(pts, posd.pmf(pts))
        return ax
    elif dist == 'cdf':
        #return posd.cdf(pts)
        ax.bar(pts, posd.cdf(pts))
        return ax
    elif dist == 'sf':
        ax.bar(pts, posd.sf(pts))
        return ax
        #return posd.sf(pts)