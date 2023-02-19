#Anonymous Function
#ไม่มีชื่อฟังก์ชัน แต่สามารถทำงานได้ปกติ

#ฟังก์ชันทั่วไป
def getcity(name):
    print(name) 

'''
#Anonymous Function = Lambda Function = FUnction แบบไม่ระบุชื่อ
lambda arguments : expression
'''
x = lambda name:print(name)
add = lambda x,y:print(x+y)
print(x("Pp"))
print(add(5,10))

def mypower(a):
    return lambda b:a**b #a=>base ,b=>เลขชี้กำลัง
y=mypower(5)
result=y(3)
print(y)
print(result)
