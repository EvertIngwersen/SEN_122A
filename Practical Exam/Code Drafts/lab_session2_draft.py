# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 15:08:59 2024

@author: evert
"""

import biogeme.database as db
import biogeme.biogeme as bio
import biogeme.biogeme_logging as blog
from biogeme import models
from biogeme.expressions import Beta, Variable, bioDraws, log, MonteCarlo, exp, bioMultSum, exp


# General packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import time
from pathlib import Path
from scipy.stats import norm, lognorm
import colorful as cf

# Pandas setting to show all columns when displaying a pandas dataframe
pd.set_option('display.max_columns', None)
try:
    logger
except NameError:    
    logger = blog.get_screen_logger(level=blog.INFO)
    print('Logger has been initialised')
    
# 1. Load the data set
data_path = Path('Norway_VTT_2009.csv')
df = pd.read_table(data_path, sep=',')
# 1. Keep only entries purpose == 5 (Long distance trips) & Mode == 1 (Car)
df = df.loc[(df['Purpose'] == 5) & (df['Mode'] == 1)]
# 2. Convert the monetary unit to euros
NOK2euro_exchange_rate = 9
df[['CostL','CostR']] = df[['CostL','CostR']] .div(NOK2euro_exchange_rate)


# Create Biogeme database object
biodata = db.Database('Norway2009VTT', df)

# Create Biogeme variable objects
CostL  = Variable('CostL')
CostR  = Variable('CostR')
TimeL  = Variable('TimeL')
TimeR  = Variable('TimeR')
Chosen = Variable('Chosen')	

switch = "02B"

match switch:
    case "3.1":
        print("3.1")
        model_name = "Norway MNL VTT-model 3.1"
        
        β_tt = Beta('β_tt', -0.1, None, None, 0)
        β_tc = Beta('β_tc', -0.1, None, None, 0)
        
        VL = TimeL*β_tt + CostL*β_tc
        VR = TimeR*β_tt + CostR*β_tc
        V = {1:VL, 2:VR}
        av = {1:1,2:1}
        
        prob = models.logit(V, av, Chosen)
        logprob = log(prob)
        
        biogeme = bio.BIOGEME(biodata, logprob)
        biogeme.nullLogLike = biogeme.calculate_null_loglikelihood(av)
        biogeme.generate_pickle = False
        biogeme.generate_html = False
        biogeme.save_iterations = False
        biogeme.modelName = model_name
        
        # Estimate the MNL model and print the results
        results = biogeme.estimate()
        print(results.print_general_statistics())
        
        # Get the results in a pandas table
        beta_hat = results.get_estimated_parameters()
        print(beta_hat)
        
        VTT_MNL = 60*(beta_hat.loc['β_tt']['Value']/beta_hat.loc['β_tc']['Value'])
        print(f'Value of travel time MNL model:  €{VTT_MNL:.2f} per hour')
    case "3.2":
        model_name = 'ML with normal distributed B_tt and B_tc'
        β_tt = Beta('β_tt', -0.1, None, None, 0)
        β_tc = Beta('β_tc', -0.1, None, None, 0)    
        σ_tt = Beta('σ_tt', 1, None, None, 0)
        σ_tc = Beta('σ_tc', 1, None, None, 0)
        
        β_tt_rnd = β_tt + σ_tt * bioDraws('β_tt_rnd', 'NORMAL_HALTON2')
        β_tc_rnd = β_tc + σ_tc * bioDraws('β_tc_rnd', 'NORMAL_HALTON2')
        
        V_L = β_tt_rnd * TimeL + β_tc_rnd * CostL
        V_R = β_tt_rnd * TimeR + β_tc_rnd * CostR   
        
        V = {1: V_L, 2: V_R}
        av = {1:1,2:1}
        
        condProb = models.logit(V, av, Chosen)
        uncondProb = MonteCarlo(condProb)
        LL = log(uncondProb)
        
        num_draws = 10
        biogeme = bio.BIOGEME(biodata, LL, number_of_draws=num_draws)
        biogeme.generate_pickle = False
        biogeme.generate_html = False
        biogeme.save_iterations = False
        biogeme.modelName = model_name
        
        results = biogeme.estimate()
        print(cf.red(results.printGeneralStatistics()))
        beta_hat = results.getEstimatedParameters()
        print(cf.green(beta_hat))     
    case "02B":
        print("case 02B")
        biodata = db.Database('Norway2009VTT',df)       
        biodata.panel('RespID')
        
        obs_per_ind = biodata.data['RespID'].value_counts().unique()[0]
        print(f'Number of observations per individual: {obs_per_ind}')
        
        df_wide = biodata.generate_flat_panel_dataframe(identical_columns=None)
        renumbered_columns = {col: f'{col.split("_")[1]}_{int(col.split("_")[0])-1}' if len(col.split("_")) == 2 else col for col in df_wide.columns}
        df_wide.rename(columns=renumbered_columns, inplace=True)
        biodata_wide = db.Database('Norway2009VTT_wide', df_wide)
        
        print(f'The wide dataset has a shape of {biodata_wide.data.shape}')
        biodata_wide.data.head()
        
        model_name = 'Panel ML WTP space with normally distributed vtt'
        vtt       = Beta('vtt',       0.4, None, None, 0)
        B_tc      = Beta('b_tc',     -0.4, None, None, 0)    
        sigma_vtt = Beta('sigma_vtt ',  2, None, None, 0)
        vtt_rnd = vtt + sigma_vtt * bioDraws('vtt_rnd', 'NORMAL_HALTON2')
        
        V_L = [B_tc * (Variable(f'CostL_{q}') + vtt_rnd * Variable(f'TimeL_{q}')) for q in range(obs_per_ind)]
        V_R = [B_tc * (Variable(f'CostR_{q}') + vtt_rnd * Variable(f'TimeR_{q}')) for q in range(obs_per_ind)]
        V = [{1: V_L[q], 2: V_R[q]} for q in range(obs_per_ind)]
        av = {1:1, 2:1}
        
        condProb = [models.loglogit(V[q], av, Variable(f'Chosen_{q}')) for q in range(obs_per_ind)] 
        condprobIndiv = exp(bioMultSum(condProb))   # exp to convert from logP to P again
        uncondProb = MonteCarlo(condprobIndiv)
        LL = log(uncondProb)
        num_draws = 10
        biogeme = bio.BIOGEME(biodata_wide , LL, number_of_draws=num_draws)
        biogeme.nullLogLike = len(biodata_wide.data)*np.log(1/2)*obs_per_ind
        biogeme.generate_pickle = False
        biogeme.generate_html = False
        biogeme.save_iterations = False
        biogeme.modelName = model_name  
        results = biogeme.estimate()
        print(results.print_general_statistics())
        
        beta_hat = results.get_estimated_parameters()
        print(beta_hat)
        VTT_WTP_ML_PANEL_normal = 60 * beta_hat.loc['vtt']['Value']
        print(f'Value of travel time Panel ML model in WTP space:  €{VTT_WTP_ML_PANEL_normal:.2f} per hour')

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        



















    
