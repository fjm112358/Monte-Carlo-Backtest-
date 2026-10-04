# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 00:15:49 2026

@author: Dylan
"""

#Setting up Monte Carlo Simulation(MCS)

nsims = 10000
hr_nmbrs = 10 

time_step = 1

start_price = float(prices.iloc[-1])
#iloc for latest price 

print("Opening price:", start_price)

np.random.seed(64)

sims = np.zeros((hr_nmbrs + 1, nsims))
sims[0] = start_price

#price paths applying geometric brownian motion equation(GBR)

for t in range(1, hr_nmbrs + 1):
    a = np.random.standard_normal(nsims)
    sims[t] = sims[t -1] * np.exp(
        (mean_rtns - 0.5 * sd_rtns**2) * time_step 
        + sd_rtns * np.sqrt(time_step) * a
        )

