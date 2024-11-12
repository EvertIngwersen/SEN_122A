# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 11:53:38 2024

@author: evert
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import biogeme.database as db
import biogeme.biogeme as bio
from biogeme import models
from biogeme.expressions import Beta, Variable, log, exp


# Create np array with the five choice tasks (TC1, TT1, TC2, TT2)
tasks = np.array([[4,35,8,25], [4,35,8,30], [6,40,7,20], [5,30,6,25], [5,40,7,20]])

# Set the number of respondents
N = 200

# Replicate the tasks N times
data = np.tile(tasks, (N, 1))

# Create respondent IDs to add to the dataframe
resp_id = np.expand_dims(np.repeat(np.arange(1, N+1), len(tasks)), axis=1)

# Create a pandas dataframe with the data
df = pd.DataFrame(np.concatenate((resp_id,data), axis=1), columns=['RESP','TC1', 'TT1', 'TC2', 'TT2'])

# Show the first 10 rows of the dataframe
df.head(10)

#create utility param

β_tt = -0.1
β_tc = -0.4
asc1 = 0
asc2 = 1

print('True decision rule: Random Utility Maximisation (RUM), with parameters:')
print(f'   β_tc: {β_tc}')
print(f'   β_tt: {β_tt}')
print(f'   asc1: {asc1}')
print(f'   asc2: {asc2}')
print(f'   --> True Value of Travel Time: {60*β_tt/β_tc:0.1f} €/hr.')

# Compute the utilities given the DGP: V = ASC + b1*TC1 + b2*TT1 + b3*TC2 + b4*TT2
df['V1'] = asc1 + β_tc * df['TC1'] + β_tt * df['TT1'] 
df['V2'] = asc2 + β_tc * df['TC2'] + β_tt * df['TT2']

# Add the error terms
# Fix the seed to make the results replicable
np.random.seed(42)
df['epsilon1'] = np.random.gumbel(size=len(df))
df['epsilon2'] = np.random.gumbel(size=len(df))

# Compute the total utility
df['U1'] = df['V1'] + df['epsilon1']
df['U2'] = df['V2'] + df['epsilon2']

# Identify the chosen alternative based on the maximum utility
df['CHOICE'] = np.nan
df.loc[df['U1'] > df['U2'], 'CHOICE'] = 1
df.loc[df['U2'] > df['U1'], 'CHOICE'] = 2

# Convert the chosen alternative to an integer (optional)
df['CHOICE'] = df['CHOICE'].astype(int)

# Save the data in a csv file
data_path =  Path(f'data/synthetic_VTTdata_tutorial1.dat')
df[['RESP','TC1', 'TT1', 'TC2', 'TT2','CHOICE']].to_csv(data_path, sep=',', index=False)

# Show the first rows
df.head()
# df.value_counts('CHOICE')

# Compute the utilities given the DGP: V = ASC + b1*TC1 + b2*TT1 + b3*TC2 + b4*TT2
df['V1'] = asc1 + β_tc * df['TC1'] + β_tt * df['TT1'] 
df['V2'] = asc2 + β_tc * df['TC2'] + β_tt * df['TT2']

# Add the error terms
# Fix the seed to make the results replicable
np.random.seed(42)
df['epsilon1'] = np.random.gumbel(size=len(df))
df['epsilon2'] = np.random.gumbel(size=len(df))

# Compute the total utility
df['U1'] = df['V1'] + df['epsilon1']
df['U2'] = df['V2'] + df['epsilon2']

# Identify the chosen alternative based on the maximum utility
df['CHOICE'] = np.nan
df.loc[df['U1'] > df['U2'], 'CHOICE'] = 1
df.loc[df['U2'] > df['U1'], 'CHOICE'] = 2

# Convert the chosen alternative to an integer (optional)
df['CHOICE'] = df['CHOICE'].astype(int)

# Save the data in a csv file
data_path =  Path(f'data/synthetic_VTTdata_tutorial1.dat')
df[['RESP','TC1', 'TT1', 'TC2', 'TT2','CHOICE']].to_csv(data_path, sep=',', index=False)

# Show the first rows
df.head()
# df.value_counts('CHOICE')



