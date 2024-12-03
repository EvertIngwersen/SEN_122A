# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 13:43:46 2024

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
N = 200
data = np.tile(tasks, (N, 1))
resp_id = np.expand_dims(np.repeat(np.arange(1, N+1), len(tasks)), axis=1)
df = pd.DataFrame(np.concatenate((resp_id,data), axis=1), columns=['RESP','TC1', 'TT1', 'TC2', 'TT2'])

#utility parameters

β_tt = -0.1
β_tc = -0.4
ASC1 = 0
ASC2 = 1

print('True decision rule: Random Utility Maximisation (RUM), with parameters:')
print(f'   β_tc: {β_tc}')
print(f'   β_tt: {β_tt}')
print(f'   ASC1: {ASC1}')
print(f'   ASC2: {ASC2}')
print(f'   --> True Value of Travel Time: {60*β_tt/β_tc:0.1f} €/hr.')

df['V1'] = ASC1 + df['TC1']*β_tc + df['TT1']*β_tt
df['V2'] = ASC2 + df['TC2']*β_tc + df['TT2']*β_tt

np.random.seed(42)
df['ε1'] = np.random.gumbel(size=len(df))
df['ε2'] = np.random.gumbel(size=len(df))

df['U1'] = df['V1']+df['ε1']
df['U2'] = df['V2']+df['ε2']

#make dataframe for choice

df['CHOICE'] = np.nan
df.loc[df['U1'] > df['U2'], 'CHOICE'] = 1
df.loc[df['U2'] > df['U1'], 'CHOICE'] = 2
df['CHOICE'] = df['CHOICE'].astype(int)
data_path =  Path(f'synthetic_VTTdata_tutorial1.dat')
df[['RESP','TC1', 'TT1', 'TC2', 'TT2','CHOICE']].to_csv(data_path, sep=',', index=False)










