#Program ค้นหา ค่ามากสุด น้อยสุด
max,min=0,9999 #กำหนดขอบเขตของโปรแกรม
while True:
    number = int(input("ENter the number :"))
    if number<0:
        break
    if number>max:
        max=number
    if number<min:
        min=number
print("Maximum value is :",max)
print("Minimum value is :",min)