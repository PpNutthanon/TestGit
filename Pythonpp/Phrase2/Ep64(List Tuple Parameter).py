#List Parameter
def displayfruit(item):
    for i in range(len(item)):
        print("Fruit",i+1,"is",item[i])

fruit=["Mango","Orange","Lemon"]
displayfruit(fruit)

#Tuple Parameter
def displayname(item):
    for i in range(len(item)):
        print("Name",i+1,"is",item[i])
name=("PP","TM","Gam")
displayname(name)
