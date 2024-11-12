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


test_numpy = np.zeros(3)