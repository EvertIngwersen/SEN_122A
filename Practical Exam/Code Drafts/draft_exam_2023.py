# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 16:16:01 2024

@author: evert
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import biogeme.biogeme as bio
import biogeme.database as db
from biogeme import models
# import biogeme.logging as blog
from biogeme.expressions import (Beta, log, exp, bioDraws, bioMultSum,MonteCarlo, Variable)
import toml
pd.set_option('display.max_columns', 500)


# # Set the number of draws in the .toml file to 150# Do not change this code
# with open('biogeme.toml', 'r') as file:
#     tomldata = toml.load(file)
# # Modify the number of draws
# tomldata['MonteCarlo']['number_of_draws'] = 150
# # Write the modified data back to the .toml file
# with open('biogeme.toml', 'w') as file:
#     toml.dump(tomldata, file)
# # Create a logger to monitor the estimation progress# if logger does not exist create it, else use it
# try:
#     logger
# except NameError:        logger = blog.get_screen_logger(level=blog.INFO)

data  = pd.read_csv('data_partial_exam_long.csv', sep='\t' )
data.head()

age = data['AGE'].value_counts()
print(age)

biodata = db.Database("Smartphone Choice", data)

#atrributes of alternative 1
COST1 = Variable('COST1')
SIZE1 = Variable('SIZE1')
STORAGE1 = Variable('STORAGE1')
CAM1 = Variable('CAM1')
OS1 = Variable('OS1')

#atrributes of alternative 2
COST2 = Variable('COST2')
SIZE2 = Variable('SIZE2')
STORAGE2 = Variable('STORAGE2')
CAM2 = Variable('CAM2')
OS2 = Variable('OS2')

#atrributes of alternative 3
COST3 = Variable('COST3')
SIZE3 = Variable('SIZE3')
STORAGE3 = Variable('STORAGE3')
CAM3 = Variable('CAM3')
OS3 = Variable('OS3')

#choice variable
CHOICE = Variable('CHOICE')















