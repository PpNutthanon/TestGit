
#Assignment รับและเรียงลำดับข้อมูลตัวเลข(มากไปน้อย หรือ น้อยไปมาก)
number=[]
while True:
    x=int(input("Enter the number :"))
    if x<0:
        break
    number.append(x) #ให้xเก็บค่าเข้าไปใน list number
print("End of the program")
print(number) #ก่อนเรียงตัวเลข
number.sort()
print(number) #หลังเรียงตัวเลข(น้อยไปมาก)
number.reverse()
print(number) #เรียงจากมากไปน้อย

#ลองทำเอง
number=[]
for i in range(10):
    x = float(input("Enter the number :"))
    number.append(x)
    number.sort()
print(number)

