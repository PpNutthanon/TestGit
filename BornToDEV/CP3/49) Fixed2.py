Systemmenu = {"Rice":45,"Fried Rice":50,"Chicken":60,"Hamburger":55}
menulist = []
def Invoice():
    print("---------Food Invoice----------")
    sum = 0
    for number in range(len(menulist)):
        print(menulist[number][0],menulist[number][1])
        sum += menulist[number][1]
    print("Total Price:", sum)

while True:
    menuname = input("Please enter your menu :")
    if (menuname.lower() == "exit"):
        break
    else:
        menulist.append([menuname,Systemmenu[menuname]])

print(menulist)
Invoice()