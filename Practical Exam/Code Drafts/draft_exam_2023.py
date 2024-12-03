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

#Socio Economic variable
AGE = Variable('AGE')

#give model name
model_name = 'Linear-additive RUM-MNL'

#model paramters
β_cost = Beta('β_cost', 0, None, None, 0)
β_size = Beta('β_size', 0, None, None, 0)
β_storage = Beta('β_storage', 0, None, None, 0)
β_cam = Beta('β_cam', 0, None, None, 0)
β_os = Beta('β_os', 0, None, None, 0)


V1 = β_cost*COST1 + β_size*SIZE1 + β_storage*STORAGE1 + β_cam*CAM1 + β_os*OS1
V2 = β_cost*COST2 + β_size*SIZE2 + β_storage*STORAGE2 + β_cam*CAM2 + β_os*OS2
V3 = β_cost*COST3 + β_size*SIZE3 + β_storage*STORAGE3 + β_cam*CAM3 + β_os*OS3

#create systematic utility dict

V = {1: V1, 2: V2, 3: V3}
av = {1:1, 2:1, 3:1}

prob = models.logit(V, av, CHOICE)
LL = log(prob)

biogeme = bio.BIOGEME(biodata,LL)

biogeme.modelName = model_name
biogeme.generatePickle = False
biogeme.generate_html = False
biogeme.saveIterations = False


#calculate nul log likelihood for rho square

biogeme.calculateNullLoglikelihood(av)
# This line starts the estimation and returns the results object.
results_MNL = biogeme.estimate()
# Print the estimation statistics
print(results_MNL.short_summary())
print(results_MNL.getEstimatedParameters())


#new model with age choice

β_cost = Beta('β_cost', 0, None, None, 0)
β_size = Beta('β_size', 0, None, None, 0)
β_storage = Beta('β_storage', 0, None, None, 0)
β_cam = Beta('β_cam', 0, None, None, 0)
β_os_young = Beta('β_os_young', 0, None, None, 0)
β_os_middle = Beta('β_os_middle', 0, None, None, 0)
β_os_old = Beta('β_os_old', 0, None, None, 0)


#new utility:
V1 = β_cost*COST1 + β_size*SIZE1 + β_storage*STORAGE1 + β_cam*CAM1 + OS1*(
    β_os_young*(AGE==1) + β_os_middle*(AGE==2) + β_os_old*(AGE==3))
V1 = β_cost*COST2 + β_size*SIZE2 + β_storage*STORAGE2 + β_cam*CAM2 + OS2*(
    β_os_young*(AGE==1) + β_os_middle*(AGE==2) + β_os_old*(AGE==3))
V3 = β_cost*COST3 + β_size*SIZE3 + β_storage*STORAGE3 + β_cam*CAM3 + OS3*(
    β_os_young*(AGE==1) + β_os_middle*(AGE==2) + β_os_old*(AGE==3))

#create systematic utility dict

V = {1: V1, 2: V2, 3: V3}
av = {1:1, 2:1, 3:1}

prob = models.logit(V, av, CHOICE)
LL = log(prob)

biogeme = bio.BIOGEME(biodata,LL)

biogeme.modelName = "Model with OS choice"
biogeme.generatePickle = False
biogeme.generate_html = False
biogeme.saveIterations = False


#calculate nul log likelihood for rho square

biogeme.calculateNullLoglikelihood(av)
# This line starts the estimation and returns the results object.
results_MNL = biogeme.estimate()
# Print the estimation statistics
print(results_MNL.short_summary())
print(results_MNL.getEstimatedParameters())
    


















