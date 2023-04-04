# Program Calculate Return on Investment of BTC in Specific Time

# Todo Import API that provide data of currency and BTC
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
from forex_python.bitcoin import BtcConverter
import datetime

# Todo Input the start_date and end_date
print("Please Enter The date Ex.21/05/2023")
print("The latest update date is 18/07/2010 - 10/07/2022")
start = input("Enter the date you start trading: ")
end = input("Enter the date you end trading: ")

# Todo Parse input dates using strptime
start_date = datetime.datetime.strptime(start, "%d/%m/%Y")
end_date = datetime.datetime.strptime(end, "%d/%m/%Y")

# Todo Set the time components to 0
start_date = start_date.replace(hour=0, minute=0, second=0, microsecond=0)
end_date = end_date.replace(hour=0, minute=0, second=0, microsecond=0)
print(start_date, end_date)

# Todo Input amount of money and currency used
currency = input("Enter the currency you use: ").upper()
capital_cost = float(input("Enter amount of money you invest: "))

# Todo Get the prices for both dates
btc_converter = BtcConverter()
currency_code = CurrencyCodes()
start_price = btc_converter.get_previous_price(currency, start_date)
end_price = btc_converter.get_previous_price(currency, end_date)
print("BTC price you bought: ", btc_converter.get_previous_price(currency, start_date), currency_code.get_symbol(currency))
print("BTC price you sold  : ", btc_converter.get_previous_price(currency, end_date), currency_code.get_symbol(currency))
print(btc_converter.get_previous_price(currency, end_date)/btc_converter.get_previous_price(currency, start_date))

# Todo Calculate profit/loss percentages and total balance
profit_loss_percentage = ((end_price - start_price) / start_price) * 100
total_balance = (capital_cost*profit_loss_percentage)/100

# Todo Check if both prices are not None and calculate the percent profit/loss
if start_price is not None and end_price is not None:
    print("Your Capital Cost: ", capital_cost, currency_code.get_symbol(currency))
    print("Total Balance: ", total_balance, currency_code.get_symbol(currency)) 
    if profit_loss_percentage > 100:
        print("Profit: ", total_balance-capital_cost, currency_code.get_symbol(currency))
    elif profit_loss_percentage <100:
        print("Loss: ", capital_cost-total_balance, currency_code.get_symbol(currency))
    else:
        print("Breakeven")
else:
    print("Prices for the given dates are not available.")

#? For now we have to find the way to change none type to float, int type in order to bring the value to calculate forward
#? For now the date doesn't up to date I need to find the latest date that I can used this API (18/07/2010 - 10/07/2022)


#! BTC Sell/BTC Buy * amount
# Todo Get price of BTC based on previous date
#btc_percent_profit_loss = b.get_previous_price(currency, end_date)/b.get_previous_price(currency, start_date)
'''
if btc_percent_profit_loss >1:
    print("Capital Cost: ", capital_cost, d.get_symbol(currency))
    print("Period of time: ", end_date - start_date)
'''


