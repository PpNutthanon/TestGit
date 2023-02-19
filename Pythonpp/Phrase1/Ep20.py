#Assignment 4 : โปรแกรมแยกเงินและหาจำนวนแบงค์
#2000 => 1000 2ใบ
#1800 => 1000 1ใบ 500 1 ใบ 100 3ใบ
money = int(input("Enter your money you want to trade(THB) :"))
#จำแนก case ในการแลกแบ้งค์(1000,500,100,50,20)

if money>=1000:
    print("1000 bath bank :",money//1000,"bank")
    money = money%1000
if money>=500:
    print("500 bath bank :",money//500,"bank")
    money = money%500
if money>=100:
    print("100 bath bank :",money//100,"bank")
    money = money%100
if money>=50:
    print("50 bath bank :",money//50,"bank")
    money = money%50
if money>=20:
    print("20 bath bank :",money//20,"bank")
    money = money%20
if money>=10:
    print("10 bath coins :",money//10,"coin")
    money = money%10
if money>=5:
    print("5 bath coins :",money//2,"coin")
    money = money%5
if money>=2:
    print("2 bath coins :",money//2,"coin")
    money = money%2
if money>=1:
    print("1 bath coins :",money//1,"coin")

#ลองทำอีกรอบ
money = int(input("Enter money you want to trade(THB) :"))
if money>=1000:
    print("The 1000 bank :",money//1000,"bank")
    money%=1000
if money>=500:
    print("The 500 bank :",money//500,"bank")
    money%=500
if money>=100:
    print("The 100 bank :",money//100,"bank")
    money%=100
if money>=50:
    print("The 50 bank :",money//50,"bank")
    money%=50
if money>=20:
    print("The 20 bank :",money//20,"bank")
    money%=20
print("Thank for using this program")