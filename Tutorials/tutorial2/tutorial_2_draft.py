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
print(cf.yellow(f"β_tt = {β_tt}"))
print(cf.yellow(f"β_tc = {β_tc}"))

