# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:21:29 2024

@author: evert
"""
from wallstreet import Stock, Call, Put
import pandas as pd
import colorful as cf
from datetime import datetime 
import time
import numpy as np
import matplotlib.pyplot as plt

start_time = datetime.now()
timeout = time.time() + 10


print("AAPL stock")
print('GOOG option - call')
g = Call('GOOG', d=3, m=11, y=2023, strike=200)

stock_list = ['AAPL', 'XOM', 'MA', 'NVO', 'SAP']


while True:
    for i in range(len(stock_list)):
        s = Stock(stock_list[i])
        price = s.price
        change = s.change
        last_trade = s.last_trade
        print()
        print(cf.yellow(s))
        if change < 0:     
            print(cf.red((f" PRICE: {price}$")))
            print(cf.red(" ΔP < 0"))
        else:
            print(cf.green((f" PRICE: {price}$")))
            print(cf.green(" ΔP > 0"))
        print("LAST TRADE", last_trade)
    if time.time() > timeout:
        print(cf.blue("MARKETS CLOSED"))
        break



