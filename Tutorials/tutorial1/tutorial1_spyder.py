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







