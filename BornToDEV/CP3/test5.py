# Program Calculate Return on Investment of BTC in Specific Time
print("----------Program Calculate Return on Investment of BTC in Specific Time----------","\n")

# Todo Import API that provide data of currency and BTC
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
from forex_python.bitcoin import BtcConverter
import datetime

# Todo Input the start_date and end_date
print("- Please Enter The date Ex.21/05/2023")
print("- The latest update date is 18/07/2010 - 10/07/2022","\n")
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
print("BTC price you sold  : ", btc_converter.get_previous_price(currency, end_date), currency_code.get_symbol(currency),"\n")

# Todo Calculate profit/loss percentages and total balance
profit_loss_percentage = round((end_price/start_price), 4)
total_balance = round((capital_cost*profit_loss_percentage), 2)

# Todo Check if both prices are not None and calculate the return on investment
print("----------Results----------")
if start_price is not None and end_price is not None:
    print("Capital Cost: ", capital_cost, currency_code.get_symbol(currency))
    print("Total Balance: ", total_balance, currency_code.get_symbol(currency)) 
    if profit_loss_percentage > 1:
        print("Profit: ", round(total_balance-capital_cost, 2), currency_code.get_symbol(currency))
    elif profit_loss_percentage < 1:
        print("Loss: ", round(capital_cost-total_balance, 2), currency_code.get_symbol(currency))
    else:
        print("Breakeven")
else:
    print("Prices for the given dates are not available.")