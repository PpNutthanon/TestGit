#Functions

#สาเหตุที่เราต้องเขียน function
a,b,c=10,23,40
if a%2==0:
    print("Even Number")
else:
    print("Odd Number")

if b%2==0:
    print("Even Number")
else:
    print("Odd Number")

if c%2==0:
    print("Even Number")
else:
    print("Odd Number")


#การสร้างและเรียกใช้งาน function
#โครงสร้าง => def ชื่อฟังก์ชัน():
#                statement
def SayHi():
    print("Hello Function")

def SayThailand():
    print("Sawasdee")

def SaySpanish():
    print("OLA")

def add():
    x=3+1
    print(x)

SayThailand() #แสดงผลเป็น Sawasdee
SaySpanish() #แสดงผลเป็น OLA
add()
for i in range(4):
     SayHi()