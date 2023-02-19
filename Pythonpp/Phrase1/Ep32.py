#Assignments ป้อนตัวเลขเพื่อหาผลรวม
#รับinput=>หาผลรวมตัวเลข5ตัว

start,stop=1,5
sum = 0
while start<=stop:
    number = int(input("Enter number :"))
    start+=1
    sum+=number
print("The summation of the number is :",sum)
print("The average of the summation is :",sum/stop)




start=1
sum = 0
stop = int(input("Enter the amount of number you want to add :"))
while start<=stop:
    number = float(input("Enter the number :"))
    sum+=number
    start+=1
print("The summation of the number :",sum)


    

