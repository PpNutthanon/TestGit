# API => Application Programming Interface
# API => ช่องทางที่นักพัฒนาโปรแกรม ออกแบบมาให้เราสามารถนำข้อมูลออกมาใช้งาน
from currency_converter import CurrencyConverter
from datetime import date
c = CurrencyConverter() #* Default Currency is EUR
print(c.convert(100,"EUR","THB"))
print(c.convert(100,"EUR"))
print(c.convert(100,"USD"))
print(c.convert(100,"EUR","USD",date=date(2010,12,21)))