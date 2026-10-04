# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 00:17:40 2026

@author: Dylan
"""

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
 