# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:45:04 2024

@author: evert
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import plotly.graph_objects as go
import biogeme.database as db
import biogeme.biogeme as bio
from biogeme import models
from biogeme.expressions import Beta, Variable, log
import colorful as cf
import vix_utils


data_path =  Path(f'data/synthetic_VTTdata_tutorial1.dat')
df = pd.read_csv(data_path)
df.head(10)

β_tt = -0.2
β_tc = -0.5

print(cf.green("Set of β's:"))
print()
print(cf.yellow(f"β_tt = {β_tt}"))
print(cf.yellow(f"β_tc = {β_tc}"))

# Compute the utilities given the set of betas 
df['V1'] = β_tt * df['TT1'] + β_tc *df['TC2']
df['V2'] = β_tt * df['TT2'] + β_tc *df['TC2']

# Compute the MNL choice probabilities using the logit formula
df['P1'] = np.exp(df['V1'])/(np.exp(df['V1']) + np.exp(df['V2']))
df['P2'] = np.exp(df['V2'])/(np.exp(df['V1']) + np.exp(df['V2']))

# Show the results
df.head()

df['P_chosen'] = (df['CHOICE']==1) * df['P1'] + (df['CHOICE']==2) * df['P2']

likelihood = df['P_chosen'].prod()
print()
print(cf.red(f"The likelihood of the data given the RUM_MNL model, with β_tt = {β_tt} and β_tc = {β_tc} is {likelihood}"))

















