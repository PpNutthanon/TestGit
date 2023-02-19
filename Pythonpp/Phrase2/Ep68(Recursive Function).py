#Recursive Function => Function เรียก Function ตัวเอง
def a():
    i=1
    print(i)
    i+=1
    a() #ทำ loop ภายใน function

def b():
    print("B")
'''
หาจุดวนซ้ำ
หาจุดออกจาก Function (return)
ต้องมี Parameter
1-5 โดยไม่ใช้คำสั่ง loop
'''
def addnumber(number):
    if number==5:
        return
    print(number) #0
    number+=1 #1
    addnumber(number)
addnumber(0)
def summation(number):
    if number==1:
        return number
    else:
        return number+summation(number-1)
x=summation(5)#5+4+3+2+1
print(x)
