#Function Input

name = input("Enter your name : ") #รับค่าที่ผู้ใช้ป้อนแล้วเก็บลงตัวแปร name
print("Hello "+name)
print(type(name))
firstname = input("Enter Your First Name : ")
lastname = input("Enter Your Lastname : ") 
print("Your first name is " + firstname)
print("Your last name is " + lastname)

x = float(input("Enter the value you want : "))
y = float(input("Enter the other value you want : "))
z = x + y #ค่อยแปลง x y เป็น float บรรทัดนี้ก็ได้แต่จะนำค่าไปใช้ต่อยอดไม่ได้
print("The sum of your value you input is",z)
print("The sum of your value you input is",x+y) #ทำแบบบรรทัด 14 หรือ 15 ก็ได้ ได้คำตอบเหมือนกัน
print(type(z))

