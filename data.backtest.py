# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 14:39:13 2026

@author: Dylan
"""

import yfinance as yf
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

#download apples data from yfinance in a 5 year period 
aapl_hrly = yf.download("AAPL",
                   period ="2y",
                   interval = "1h"
                   )

#printsfirst ten 
print(aapl_hrly.shape)

prices = aapl_hrly["Close"].squeeze()

print(prices.head(5))

#Hourly return by applying HRR

returns = prices.pct_change().dropna()

print(returns.head(5))

#Mean and median 

mean_rtns = returns.mean()
sd_rtns = returns.std()

rnd_mean_rtn = np.round(mean_rtns, decimals = 6)
rnd_sd_rtn = np.round(sd_rtns, decimals = 6)

print( "Mean Hourly return:", mean_rtns )
print("Volatility(Hourly):", sd_rtns)
print("Mean(4dp):", rnd_mean_rtn)
print("Volatility(4dp):", rnd_sd_rtn)
#providing raw and clean data 
