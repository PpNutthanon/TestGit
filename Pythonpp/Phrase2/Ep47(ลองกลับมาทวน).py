#Assignment การจับคู่สินค้ากับราคา
fruit=["mango","banana","orange","watermelon"]
price=[50,30,15,25]

for x,y in zip(fruit,price[::-1]):
    print("Menu:",x,"Price:",y)
