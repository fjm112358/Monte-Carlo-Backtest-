# Monte-Carlo-Backtest


This project uses the Monte Carlo simulation to model future stock pricing and estimate probabilities  of price increases or decreases. The model then uses signals that are backtested with previous data. 



## Technology-Used 
*Python - Coding language used for backtest
*numpy - library used for mathematical tools
*matplotlib - library used to display mathematical data using plots
*Pandas - library used to clean data imported from yfinance
*yfinance - library containing finacial data

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
[!WARNING]
> **Large simulations take longer run.** Increasing the number of simulations, historical data, or holding periods will increase the processing time so if your data i'snt loading then give it time to load.

