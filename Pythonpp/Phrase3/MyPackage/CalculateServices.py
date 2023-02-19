#สร้างฟังก์ชันเกี่ยวกับคณิตศาสตร์
#ให้บิรการข้อมูลค่าคงที่/คำนวณตัวเลข
PI=3.14
Root2=1.414
def addition(*args):
    total=0
    for i in range(len(args)):
        total+=args[i]
    print("The Addition Of The Number Is :",total)

def subtract(a,b):
    print("The Value Of Substraction Is :",a-b)