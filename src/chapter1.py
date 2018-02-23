import pandas as pd
import numpy as np
from scipy.stats import trim_mean

def weighted_median(df,value_column=None,weight_column=None):
    tmp = df.sort_values(by=value_column)
    cumsum = df[weight_column].cumsum()
    cutoff = df[weight_column].sum() / 2.0
    return df[value_column][cumsum >= cutoff].iloc[0]

state = pd.read_csv('../data/state.csv')
print(state['Population'].mean())
print(trim_mean(state['Population'], proportiontocut=0.1))
print(state['Population'].median())

print(np.average(state['Murder.Rate'], weights=state['Population'])
print(weighted_median(state,'Murder.Rate','Population'))

