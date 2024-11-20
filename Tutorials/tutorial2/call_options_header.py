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
timeout = time.time() + 200

print('\n Initializing a text using\
    the Explicit multi-line statement')

print("AAPL stock")
print('GOOG option - call')
g = Call('GOOG', d=3, m=11, y=2023, strike=200)

stock_list = ['AAPL', 'XOM', 'MA', 'NVO', 'SAP']

ΔP_dict = {}
keys = range(len(stock_list))

for i in keys:
    ΔP_dict[i] = stock_list[i]

print(ΔP_dict)



ΔP_matrix = np.zeros((5,1))

for i in range(len(stock_list)):
    ΔP_matrix[i,0] = i

change_list_AAPL = []
change_list_XOM = []
change_list_MA = []
change_list_NVO = []
change_list_SAP = []

while True:
    for i in range(len(stock_list)):
        print("-------------------")
        s = Stock(stock_list[i])
        price = s.price
        change = s.change
        ΔP_matrix[i,0] = change
        last_trade = s.last_trade
        print(cf.yellow(s))
        if i == 0:
            change_list_AAPL.append(change)
            average = sum(change_list_AAPL)/len(change_list_AAPL)
            print(cf.yellow(f"AVG ΔP = {average}"))
        if i == 1:
            change_list_XOM.append(change)
            average = sum(change_list_XOM)/len(change_list_XOM)
            print(cf.yellow(f"AVG ΔP = {average}"))
        if i == 2:
            change_list_MA.append(change)
            average = sum(change_list_MA)/len(change_list_MA)
            print(cf.yellow(f"AVG ΔP = {average}"))
        if i == 3:
            change_list_NVO.append(change)
            average = sum(change_list_NVO)/len(change_list_NVO)
            print(cf.yellow(f"AVG ΔP = {average}"))
        if i == 4:
            change_list_SAP.append(change)
            average = sum(change_list_SAP)/len(change_list_SAP)
            print(cf.yellow(f"AVG ΔP = {average}"))
        if change < 0:     
            print(cf.red((f" PRICE: {price}$")))
            print(cf.red(" ΔP < 0"))
            print(cf.red(f" CHANGE: {change}$"))
            print(cf.red("UTILITY LEVEL = LOW"))
            print()
        else:
            print(cf.green((f" PRICE: {price}$")))
            print(cf.green(" ΔP > 0"))
            print(cf.green(f" CHANGE: {change}$"))
            print(cf.green("UTILITY LEVEL = HIGH"))
        print("LAST TRADE", last_trade)
    if time.time() > timeout:
        print(cf.blue("MARKETS CLOSED"))
        break



