# Continue => คำสั่งให้มีการ ข้ามคำสั่งต่อไป ใน loop for รอบนั้นๆ
start = int(input("Enter The Multiplication Table Start :"))
stop = int(input("Enter The Multiplication Table Stop :"))
for i in range(start,stop+1):
    print("Multiplication Table :",i)
    for j in range(1,13):
        print(i,"X",j,"=",i*j)
    break

for i in range(start,stop+1):
    break
    print("Multiplication Table :",i)
    for j in range(1,13):
        print(i,"X",j,"=",i*j)

for val in "Hello":
    print(val)
print("The End")

for val in "Hello":
    if val == "l":
        continue
    print(val)
print("The End")