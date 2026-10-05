# Monte-Carlo-Backtest

## Overview 
Monte Carlo simulation is a computational method that uses repeated random sampling to model a range of possible outcomes. In this project, Monte Carlo simulation is used to generate potential future AAPL stock prices based on historical hourly returns and volatility. The project historical AAPL price data using yfinance and calculates hourly returns using pandas and NumPy. The historical mean return and standard deviation are then used as inputs for the simulation. Thousands of possible future price paths are generated, allowing the distribution of potential future prices to be analysed.

![Monte Carlo Simulation](MCSbroomstick.png)

To better understand the Simulation we can use a normal distribution. The bell curve shows that most simulated outcomes are close to the expected outcome as well as showing; 

*Increasingly extreme outcomes becoming less likely, 
*Most simulations produce moderate price movements 
*Fewer simulations produce large positive or negative movements

![Bellcurve](Bellcurve.png)

This is useful because the purpose of Monte Carlo simulation is not to predict one exact future price, but to model a range of plausible outcomes and estimate their probabilities.

## Results 
Strategy was backtested using historical AAPL hourly data. For each historical observation, 1,000 Monte Carlo simulations were generated using Geometric Brownian Motion. The percentage of simulations where the final simulated price exceeded the current price was used as the probability of an upward movement.Trading signals were generated using probability thresholds of 51%, 55%, 60%, 65%, and 70%, with holding periods ranging from 1 to 30 hours.

### Analysis

![BacktestResults](Backtestresults.png)

Results show that the 51% threshold produced the strongest performance across the tested parameters. Increasing the holding period at this threshold increased the sum of trade returns:

* 1 hour: −8.16%, 48.40% win rate
* 5 hours: 73.87%, 54.17% win rate
* 10 hours: 149.76%, 53.95% win rate
* 20 hours: 293.45%, 53.68% win rate
* 30 hours: 542.85%, 56.52% win rate

Higher probability thresholds resulted in substantially fewer trades and generally negative returns. For example, the 60% threshold produced negative returns across every holding period where trades occurred, while the 65% and 70% thresholds generated almost no trades.This suggests that, within this particular backtest, a lower probability threshold combined with a longer holding period produced more favourable results. However, the results should not be interpreted as guaranteed future performance, and the sum of trade returns does not represent a fully capitalised portfolio return. 

## Technology-Used 
* Python - Coding language used for backtest
* numpy - library used for mathematical tools
* matplotlib - library used to display mathematical data using plots
* Pandas - library used to clean data imported from yfinance
* yfinance - library containing finacial data

## How-to-Use
Can either paste or download the raw code from the repository and download the imported libraries 

```bash
pip install pandas numpy matplotlib yfinance openpyxl
Then run:
```
```bash
python backtest(mcs).raw.y
```
this allows you to play with the code, use different numbers, plots or data as well access to the plots.

> **Large simulations take longer run.** Increasing the number of simulations, historical data, or holding periods will increase the processing time so if your data i'snt loading then give it time to load.

