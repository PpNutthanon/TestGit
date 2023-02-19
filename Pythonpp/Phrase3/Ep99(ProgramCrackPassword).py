#Crack Password
#Password ATM = 132
import random
password=input("Enter The Password :")
result=""
while result!=password:
    result=""
    for letter in range(len(password)):
        listnumber=random.choice("0123456789abcdefgp")
        result="".join(listnumber)+str(result)
        print("Search =",result)
print("Crack Password Is :",result)
