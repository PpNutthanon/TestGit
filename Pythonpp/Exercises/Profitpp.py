print("Table for profit")
money = float(input("Your Initial Money :"))
profit = float(input("How many profit do you want(%) :"))
profit = 1+(profit/100)
day = int(input("Enter how many day do you want to take profit :"))
for i in range(1,day+1):
    print("Money initial day",i,":",money)
    money*=profit
    print("Money final day",i,":",money)

