#Function Return
'''
1)ไม่มีการรับค่าและส่งค่า
def name():
2)มีการรับค่าส่งเข้าไปทำงาน
def name(a,b):
3)การรับค่าเข้าไปทำงาน และส่งออกมา
def name(a,b):
    return a+b
4)ไม่มีการรับค่าเข้ามา แต่ส่งค่าออกไป

'''
def add(a,b):
    return a+b
def shownumber():
    return 500
a=shownumber()
print(a)
print(shownumber())
x=add(10,20)
print(x)
print(add(10,20))

def randomnumber(b):
    if x=="100":
        print("You won the lottery")
        return 1000
    else:
        print("Sorry your luck not today")
        return 0
money=randomnumber(200)
print("Money =>",money)

