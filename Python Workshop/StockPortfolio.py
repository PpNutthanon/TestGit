#Build The Portfolio Visualization
import datetime as dt 
import matplotlib.pyplot as plt 
import pandas_datareader as web 

#? Assume The Variables
tickers = ["AAPL","TSLA","FB","NVDA","AMZN","GOOG"]
amounts = [7,5,12,16,2,4]
prices = []
total = []

for ticker in tickers:
    df = web.DataReader(ticker,"yahoo",dt.datetime(2019,8,1), dt.datetime.now())
    price = df[-1:]["close"][0]
    prices.append(price)
    index = tickers.index((ticker))
    total.append(price*amounts[index])

#*Todo Visualize Stock Portfolio
