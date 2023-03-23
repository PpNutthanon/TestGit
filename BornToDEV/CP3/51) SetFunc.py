fruits = {"Apple","Banana","Orange","Pineapple"}
print(fruits)
fruits.remove("Apple")
print(fruits)
fruits.add("Watermelon")
print(fruits)
 
Userinput = int(input("Enter Number of The Fruits:"))
myfruit = set()
while(len(myfruit) < Userinput):
    myfruit.add(input("Fruits: "))
    print(myfruit)
