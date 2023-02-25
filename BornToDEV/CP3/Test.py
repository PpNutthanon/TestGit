print("Program Create Triangle")
print("-------------------------------")
number = int(input("Enter The Level of Triangle :"))
for i in range(1,number):
        print(" "*(number-i)+"*"*((2*i)-1))
        