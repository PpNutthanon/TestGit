menulist = []
pricelist = []
def Invoice():
    print("---------My Food Invoice----------")
    for number in range(0,len(pricelist)):
        print(menulist[number],pricelist[number])
    print("Total Price: ",sum(pricelist))

while True:
    menu = input("Please Enter Your Menu: ")
    menulist.append(menu)
    if menu.lower() == "exit":
        break
    else:
        price = int(input("Enter Price: "))
        pricelist.append(price)

Invoice()