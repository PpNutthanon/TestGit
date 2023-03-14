menulist = []
def Invoice():
    print("---------Food Invoice----------")
    sum = 0
    for number in range(0,len(menulist)):
        print(menulist[number][0], menulist[number][1])
        sum += menulist[number][1]
    print("Total Price:", sum)


while True:
    menu = input("Please Enter Your Menu: ")
    if menu.lower() == "exit":
        break
    else:
        price = int(input("Enter Price: "))
        menulist.append([menu,price])

print(menulist[0][1]+menulist[1][1])
print(menulist)
Invoice()