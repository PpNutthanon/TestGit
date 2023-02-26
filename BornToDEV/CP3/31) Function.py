# Function(def) => กลุ่มของคำสั่ง ที่มีจุดมุ่งหมายเดียวกัน
def SayHi():
    print("Hello World!")
    SayName(name)

def SayName(name):
    print("Hello",name)

name  = input("Enter name: ")
SayHi() #TODO เรียกใช้งานฟังก์ชัน SayHi
SayName(name)