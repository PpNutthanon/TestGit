menulist = []


def Invoice():
    print("---------My Food Invoice----------")
    for number in range(0,len(menulist)):
        print(menulist[number])

while True:
    menu = input("Please Enter Your Menu: ")
    if menu.lower() == "exit":
        break
    else:
        price = int(input("Enter Price: "))
        menulist.append([menu,price])

print(menulist)
Invoice()