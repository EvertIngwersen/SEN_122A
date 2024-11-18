# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 15:44:11 2024

@author: evert
"""

# Biogeme
import biogeme.database as db
import biogeme.biogeme as bio
from biogeme import models
from biogeme.expressions import Beta, Variable, log, exp

# General python packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from pathlib import Path

# Pandas setting to show all columns when displaying a pandas dataframe
pd.set_option('display.max_columns', None)

# Create that path to the data file
data_path =  Path(f'data/choice_data_cleaned.dat')
df = pd.read_csv(data_path, sep='\t')

attributes =   ['STORES1', 'TRANSPORT1', 'CITY1', 'NOISE1', 'GREEN1', 'FOREIGN1', 
                'STORES2', 'TRANSPORT2', 'CITY2', 'NOISE2', 'GREEN2', 'FOREIGN2',
                'STORES3', 'TRANSPORT3', 'CITY3', 'NOISE3', 'GREEN3', 'FOREIGN3']
round(df[attributes].describe(),2)

# Counts the number of times each  alternative is chosen
choice_freq = df['CHOICE'].value_counts()

# Calculate the percentage of the chosen alternatives
choice_percent = round(choice_freq / len(df['CHOICE']) * 100,2)

# Table Summary
choice_table = pd.DataFrame({'Choice': choice_freq.index, 'Frequency': choice_freq.values, 'Percentage':choice_percent.values} )

# Show the table
choice_table

"""
When modelling choice behaviour, 
it is also important to have a good understanding of whether the sample 
(i.e. the collected data) is representative of the target population. 
If you are working with a non-representative sample, 
the results and conclusions can not be generalised to the population. 
This is particularly important when the objective is to 
determine e.g. Willingness-to-pay estimates.=

To assess whether the sample is representative of our target population, 
we compare the sample statistics of the socio-demographic variables with statistics of the population. 
Usually, population statistics are made available by the National Bureaus of Statistics. 
In the Netherlands, this institute is called CBS (Centraal Bureau voor de Statistiek).

Explore the sample statistics.<br>

`A` Identify the column with socio-demographic variables 
`B` Use the describe() to describe the socio-demographic variables, and create histograms for the variables
`C` Reflect on the representativeness of the sample, without comparing them to the population statistics<


"""






















