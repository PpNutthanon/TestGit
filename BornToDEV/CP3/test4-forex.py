from forex_python.converter import CurrencyRates
import datetime

# Todo List all latest currency rates
c = CurrencyRates()
currency_name1 = input("Enter the currency symbol 1: ").upper()
currency_name2 = input("Enter the currency symbol 2: ").upper()
print("Currency 1:", currency_name1)
print("Currency 2:", currency_name2)
print(c.get_rates(currency_name1))

# Todo List all currency rates in the specific date
date_obj = datetime.datetime(2017, 5, 23, 18, 36, 28, 151012)
print(c.get_rates(currency_name1, date_obj))

# Todo Get Conversion rate from _ to _
print(c.get_rate("USD", "THB"))

# Todo Convert amount from __ to __
print(c.convert(currency_name1, currency_name2, 100.45))

# Todo Convert amount from __ to __ based on 2017-05-23 exchange rates:
print(c.convert(currency_name1, currency_name2, 100.45, date_obj))

# Todo Get lastest price of 1 BTC
from forex_python.bitcoin import BtcConverter
b = BtcConverter()
print(b.get_latest_price("USD"))

# Todo Get price of BTC based on previous date
date_obj2 = datetime.datetime(2016, 5, 18, 19, 39, 36, 815417)
print(b.get_previous_price("USD",date_obj2))

# Todo Convert Amount to BTC
print(b.convert_to_btc(5000,"USD"))

# Todo Convert amount BTC based on previous date price
print(b.convert_to_btc_on(5000, 'USD', date_obj))