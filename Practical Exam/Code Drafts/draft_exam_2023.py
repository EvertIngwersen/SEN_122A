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



