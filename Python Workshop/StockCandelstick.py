#Visualize Stock Data With Candlestick Charts

#? Import Machine Learning To The Editor
import datetime as dt 
import pandas_datareader as web 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc

#*todo Set The Time We Want To See
start=dt.datetime(2019,1,1) #! You Can Pick Date You Want
end=dt.datetime.now()

#* Load Datas
ticker = "FB" #! You Can Change The Name Of The Stock
data= web.DataReader(ticker, "yahoo", start, end) 

#? Restructures Datas
data = data[["Open","High","Low","Close"]]
data.reset_index(inplace=True)
data["Date"] = data["Date"].map(mdates.date2num)
print(data.head())

#*Todo Plot The Data of Stock & Visualization
ax = plt.subplot()
ax.grid(True)
ax.set_axisbelow(True)
ax.set_title("{} Share Price".format(ticker),color="white")
ax.set_facecolor("black")
ax.figure.set_facecolor("#121212")
ax.tick_params(axis="x",colors="white")
ax.tick_params(axis="y",colors="white")
ax.xaxis_date()
candlestick_ohlc(ax, data.values, width=0.5, colorup="#00ff00")
plt.show()