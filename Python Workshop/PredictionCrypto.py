#Import Machine Learning & Function 
import datetime as dt
import numpy as np
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt

#? Import Deep Learning To IDE
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.models import Sequential
from tensorflow.python.keras.engine import sequential

#*todo Assume Which Pair Currency Want To Predict
crypto_currency = "BTC"
against_currency = "USD"

#* Set Period of Datetime That Use To Predict Price Of BTC
start = dt.datetime(2016,1,1)
end = dt.datetime.now()

#! Look For The Trainning Data
data=web.DataReader(f"{crypto_currency}-{against_currency}","yahoo",start,end)

#Prepare Data From Neural Network
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(data["Close"].values.reshape(-1,1))

#? Pick The Prediction Date Want To Predict
prediction_days = 60
x_train, y_train =[], []

#*Todo Fill Those Lists Of Actual Values
for x in range(prediction_days,len(scaled_data)):
    x_train.append(scaled_data[x-prediction_days:x, 0])
    y_train.append(scaled_data[x, 0])
x_train, y_train = np.array(x_train), np.array(y_train) #Change Lists To Array Datatype
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

#* Create The Neural Network Models To Prediction
#! pip install numpy==1.19.5
model = Sequential()

#Add ASTM Layers & Dropout Layers
model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50))
model.add(Dropout(0.2))
model.add(Dense(units=1))
model.compile(optimizer="adam", loss="mean_squared_error")
model.fit(x_train, y_train, epochs=25, batch_size=32)

#? Testing The Model Of Prediction
test_start = dt.datetime(2020,1,1)
test_end = dt.datetime.now()
test_data=web.DataReader(f"{crypto_currency}-{against_currency}","yahoo", test_start, test_end)
actual_prices = test_data["Close"].values
total_dataset = pd.concat((data["Close"], test_data["Close"]), axis=0)

#*Todo Get The Model To Use For The Prediction
model_inputs = total_dataset[len(total_dataset)-len(test_data)-prediction_days:].values
model_inputs = model_inputs.reshape(-1,1)
model_inputs = scaler.fit_transform(model_inputs)

#! Make Some Prediction Using The Train Model
x_test=[]
for x in range(prediction_days, len(model_inputs)):
    x_test.append(model_inputs[x-prediction_days:x, 0])
x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

#* Find The Prdiction Prices
prediction_prices = model.predict(x_test)
prediction_prices = scaler.inverse_transform(prediction_prices)

#? Visualize To The Graph
plt.plot(actual_prices, color="black", label="Actual Prices")
plt.plot(prediction_prices, color="green", label="Prediction Prices")
plt.title(f"{crypto_currency} price prediction")
plt.xlabel("Time")
plt.ylabel("Price")
plt.legend(loc="upper left")
plt.show()