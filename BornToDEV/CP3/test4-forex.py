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

# Todo Convert BTC to Valid currency amount based on lates prices
print(b.convert_btc_to_cur(1.25,"USD"))

# Todo Convert BTC to valid currency amount based on previous date price
date_obj3 = datetime.datetime(2016,5,18,19,38,36,815417)
print(b.convert_btc_to_cur_on(1.25,"EUR", date_obj3))

# Todo Get list of prices list for given date range
start_date = datetime.datetime(2016,5,18,19,39,36,81547)
end_date = datetime.datetime(2016,5,23,19,39,36,815417)
print(b.get_previous_price_list("BTC",start_date, end_date))

# Todo Get BTC Symbol or any Currency symbol
print(b.get_symbol())

# Todo Get Currency Symbol and Name using currency code
from forex_python.converter import CurrencyCodes
d = CurrencyCodes()
print(d.get_symbol("EUR"))
print(d.get_currency_name("EUR"))


#! Find Return on Investment If You Start Invest in BTC from __ to __

#! Forex Trading Simulation