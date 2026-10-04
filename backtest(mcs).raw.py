# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 17:11:52 2026

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

#broom stick model 
plt.figure(figsize=(11, 7))
plt.plot(sims[:, :500], alpha=0.4)
plt.axhline(start_price, linestyle="-", alpha = 1, label="Starting price")
plt.title("AAPL Broomstick model")
plt.xlabel("Hours into the future")
plt.ylabel("Simulated share price")
plt.legend()
plt.show()

final_prices = sims[-1, :]

#raw
mean_final = np.mean(final_prices)
med_final = np.median(final_prices)
lwr_bnd = np.percentile(final_prices, 5)
uppr_bnd = np.percentile(final_prices, 95)

#shows mcs follows bell curve 
plt.figure(figsize=(11, 7))
plt.hist(final_prices, bins=100, alpha=0.7, 
         edgecolor = "Blue", linewidth = 1.2 )
plt.axvline(start_price, linestyle="--", label="Starting price")
plt.axvline(mean_final, linestyle="--", label="Mean final price")
plt.title("AAPL Price Distribution")
plt.xlabel("Simulated final price")
plt.ylabel("Number of simulations")
plt.legend()
plt.show()
 
#clean   
rnd_mean_final = np.round(mean_final, decimals=6)
rnd_med_final = np.round(med_final, decimals=6)
rnd_lwr_bnd = np.round(lwr_bnd, decimals=6)
rnd_uppr_bnd = np.round(uppr_bnd, decimals=6)

#clean data for dispaly, will use raw data in calculations 
print("Mean final price:", rnd_mean_final)
print("Median final price:", rnd_med_final)
print("5th percentile:", rnd_lwr_bnd)
print("95th percentile:", rnd_uppr_bnd)

#probability of a price increase
prob_up = np.mean(final_prices > start_price)
prob_down = np.mean(final_prices < start_price)

print("Probability of price increase:", round(prob_up * 100, 2),"%")
print("Probability of price decrease:", round(prob_down * 100, 2),"%")

#log better fit
log_rtns = np.log(prices / prices.shift(1)).dropna()

print("Historical observations:", len(log_rtns))


#settings 
thrshlds = [0.51, 0.55, 0.60, 0.65, 0.70]
hldng_periods = [1, 5, 10, 20, 30]

# multiple thresholds and holdings allow us to see what pairs could work best
# we can run yet another Monte Carlo simulation
nsims_strat = 1000  # this is not the same as above as this is the strategy
lookbck_hrs = 1000  # hours used to estimate

# create a list to store results
results = []

# use for loop to loop through every threshold and every holding period
for thrshld in thrshlds:
    for hldng_period in hldng_periods:
        trde_rtns = []
        for i in range(lookbck_hrs, len(prices) - hldng_period):
            crrnt_prce = float(prices.iloc[i])
            historical_rtns = log_rtns.iloc[i - lookbck_hrs:i]
        
            #Mean and variance(volatility)
            #raw
            mean_historical_rtns = historical_rtns.mean()
            sd_historical_rtns = historical_rtns.std()
           #Clean 
            rnd_mean_historical_rtns = np.round(mean_historical_rtns, decimals=6)
            rnd_sd_historical_rtns = np.round(sd_historical_rtns, decimals=6)
            #raw values used in calculations

            #MCS
            time_step = 1
            hr_nmbrs = hldng_period
            sims = np.zeros((hr_nmbrs + 1, nsims_strat))

            # All simulations start at the current historical price
            sims[0] = crrnt_prce

            #GBM equation
            for t in range(1, hr_nmbrs + 1):
                a = np.random.standard_normal(nsims_strat)
                sims[t] = sims[t - 1] * np.exp(
                    (mean_historical_rtns - 0.5 * sd_historical_rtns**2)* time_step
                    + sd_historical_rtns* np.sqrt(time_step) * a
                )

            #Probability of price increase
            #Prices at the end of the holding period
            final_prices = sims[-1, :]
            probability_up = np.mean(final_prices > crrnt_prce)
                
            #Buy if probability exceeds threshold
            if probability_up >= thrshld:
                future_price = float(prices.iloc[i + hldng_period])
                trde_rtn = (
                    future_price - crrnt_prce
                ) / crrnt_prce
                trde_rtns.append(trde_rtn)

        if len(trde_rtns) > 0:
            trde_rtns = np.array(trde_rtns)
            total_return = np.sum(trde_rtns)
            average_return = np.mean(trde_rtns)
            win_rate = np.mean(trde_rtns > 0)
            number_trades = len(trde_rtns)

        else:
            total_return = 0
            average_return = 0
            win_rate = 0
            number_trades = 0
        
        # Store resultsthreshold and holding period
        results.append({
            "Threshold": thrshld,
            "Holding Period(Hrs)": hldng_period,
            "Trades": number_trades,
            "Sum of Trade Returns": total_return,
            "Average Trade Return": average_return,
            "Win Rate(%)": win_rate
        })

#results table
results_df = pd.DataFrame(results)

#Plotiing results 
table_df = results_df.copy()

table_df["Threshold"] = table_df["Threshold"].map(
    lambda x: f"{x:.2f}"
    )
table_df["Sum of Trade Returns"] = table_df["Sum of Trade Returns"].map(
    lambda x: f"{x * 100:.2f}%"
    )
table_df["Average Trade Return"] = table_df["Average Trade Return"].map(
    lambda x: f"{x * 100:.2f}%"
    )
table_df["Win Rate(%)"] = table_df["Win Rate(%)"].map(
    lambda x: f"{x * 100:.2f}%"
    )

fig, ax = plt.subplots(figsize=(12, 4))
ax.axis("off")
table = ax.table(
    cellText=table_df.values,
    colLabels=table_df.columns,
    cellLoc="center",
    loc="center"
)
table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1, 2)

plt.tight_layout()
plt.show()



