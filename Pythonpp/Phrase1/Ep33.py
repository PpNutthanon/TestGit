#Assignmet หาผลรวมตัวเลข(ปรับเงื่อนไข)
sum = 0
start = 1
stop = int(input("Enter amount of number you want to add :"))
while start<=stop:
    number = float(input("Enter number :"))
    start+=1
    sum+=number
    if sum>100:
        break
print("The summation is :",sum)

#ทำตามในคลิป
sum = 0
while sum<100:
    number = int(input("Enter the number :"))
    sum+=number
    print("The summation is :",sum)



