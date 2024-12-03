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

biodata = db.Database('synthetic_VTTdata', df)

# We create Variable objects for each of the variables in the data set that we want to use in the model
# Attributes of alternative 1
TT1  = Variable('TT1')
TC1  = Variable('TC1')

# Attributes of alternative 2    
TT2  = Variable('TT2')
TC2  = Variable('TC2')

# The choice
CHOICE = Variable('CHOICE')

# Give a name to the model    
model_name = 'Linear-additive RUM-MNL with ASC (true model)'

# Define the model parameters, using the function "Beta()", in which you must define:
# the name of the parameter,
# starting value, 
# lower bound,
# upper bound, 
# 0 or 1, indicating if the parameter must be estimated. 0 means estimated, 1 means fixed to the starting value. 
B_TT = Beta('B_TT', 0, None, None, 0)
B_TC = Beta('B_TC', 0, None, None, 0)
ASC1 = Beta('ASC1', 0, None, None, 1)
ASC2 = Beta('ASC2', 0, None, None, 0)

# Define the utility functions
V1 = ASC1 + B_TT * TT1 + B_TC * TC1
V2 = ASC2 + B_TT * TT2 + B_TC * TC2

# Create a function to estimate an MNL models with two alternatives
def estimate_mnl(V1,V2,CHOICE,database,model_name):

    V = {1: V1, 2: V2}
        
    # Create a dictionary called av to describe the availability conditions of each alternative, where 1 indicates that the alternative is available, and 0 indicates that the alternative is not available.
    # This shows that all alternatives were available to all respondents. 
    av = {1: 1, 2: 1} 

    # Define the choice model: The function models.logit() computes the MNL choice probabilities of the chosen alternative given the V. 
    prob = models.logit(V, av, CHOICE)

    # Define the log-likelihood   
    LL = log(prob)

    # Create the Biogeme object containing the object database and the formula for the contribution to the log-likelihood of each row using the following syntax:
    biogeme = bio.BIOGEME(database, LL)

    # The following syntax passes the name of the model:
    biogeme.modelName = model_name

    # Some object settings regaridng whether to save the results and outputs 
    biogeme.generate_pickle = False
    biogeme.generate_html = False
    biogeme.save_iterations = False

    # Syntax to calculate the null log-likelihood. The null-log-likelihood is used to compute the rho-square 
    biogeme.calculate_null_loglikelihood(av)

    # This line starts the estimation and returns the results object.
    results_MNL = biogeme.estimate()

    return results_MNL

# Estimate the model
results_MNL = estimate_mnl(V1,V2,CHOICE,biodata,model_name)

# Print the estimation statistics
print(results_MNL.short_summary())

# Print model parameters
print(results_MNL.get_estimated_parameters()) 

# Calculate the value of travel time and print it
VTT = 60*(results_MNL.get_beta_values()['B_TT']/results_MNL.get_beta_values()['B_TC'])
print(f'\nThe Value of Travel Time is: {VTT:.2f} €/hr.')


