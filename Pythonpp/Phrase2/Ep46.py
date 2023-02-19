#Assignment หาค่าเลขยกกำลัง
number=[]
round=int(input("Enter how many number you want to add:"))
for i in range(round):
    x = float(input("Enter the number:"))
    number.append(x)
    number[i]=number[i]**2
number.sort()
print(number)

#ทำแบบลดรูป number=[i*i for i in number]


#ลองทำเอง
number=[]
round = int(input("How many number do you want to add:"))
for i in range(round):
    x = float(input("Enter the number:"))
    number.append(x)
    number[i]=number[i]**2
print(number)