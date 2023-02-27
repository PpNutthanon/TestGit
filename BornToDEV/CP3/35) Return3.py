def login():
    User = input("Username :")
    Password = input("Password :")
    if User == "admin" and Password == "PP":
        return True
    else:
        return False
    
def showmenu():
    print("-----Pp Shop-----")
    print("1) VAT Calculator")
    print("2) Price Calculator")

def menuselect():
    select = int(input("Enter number : "))
    return select

def VAT(totalprice):
    VAT = 0.07
    result = totalprice*(1+VAT)
    return result

def Price():
    price1 = int(input("Enter the price :"))
    price2 = int(input("Enter the price :"))
    return VAT(price1+price2)

    
print(Price())

#Login
#Show Menu
#Select Menu
#VAT
#Price