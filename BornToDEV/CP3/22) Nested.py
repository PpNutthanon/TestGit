# Nested Condition => เงื่อนไขซ้อนเงื่อนไข
if False:
    print("Hello Welcome :")
    if True:
        print("YO Mr.A")
        if True:
            print("Haha")

User = input("Username :")
Password = input("Password :")
if User == "admin" and Password == "PP":
    print("Done")
    print("-----Pp Shop-----")
    print("1) VAT Calculator")
    print("2) Price Calculator")
    select = int(input("Enter number : "))
    if select == 1:
        price = float(input("Enter the price :"))
        VAT = 0.07
        result = price*(1+VAT)
        print(result)
    elif select == 2:
        price1 = int(input("Enter the price :"))
        price2 = int(input("Enter the price :"))
        print(price1+price2)
else:
    print("Incorrect Password")
