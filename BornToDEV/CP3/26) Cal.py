sum = 0
round = int(input("Enter the round of sum :"))
for i in range(round):
    number = float(input("Enter the "+str(i+1)+" number :"))
    sum = sum + number
print("The Sum of the Number :",sum)