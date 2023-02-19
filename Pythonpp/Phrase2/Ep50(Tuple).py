#Tuple => เหมือน list แต่ไม่สามารถเปลี่ยนแปลงข้อมูลได้
#นำไปใช้ได้กับ เช่น id,รหัสบัตรประชาชน,ค่าคงที่

#การนิยาม(constructor กับ แบบทั่วไป)
tup=(1,True,"Nutthanon",34.58) #สัญลักษณ์ของ tuple
lis=[1,True,"Nutthanon"] #สัญลักษณ์ของ list
print(tup)
print(lis)
print(type(tup))
print(type(lis))

#การแก้ไขข้อมูล
a=tuple((1,2,3,4))
b=list([1,2,3,4])
b[0]=20
print(b)

#การเข้าถึงข้อมูล
print(tup[0:3])
print(tup[-1])
print(tup[1:]) #ไล่ตั้งแต่index1 ถึงสมาชิกตัวสุดท้าย
print(a[-2])
print(b[-3:])

#การแก้ไขข้อมูล
lis=list(tup)
lis[0]="PP"
tup=tuple(lis)
print(tup)

#การแสดงผลด้วย loop
for item in tup:
    print("The member is :",item) 

#การตรวจสอบข้อมูล
if "apo" in tup:
    print("It is member")
else:
    print("Not a member")
if "PP" in tup:
    print("It is member")
else:
    print("Not a member")

#การนับสมาชิก
print(len(tup)) #len4 Index3

#การใช้ len ทำงานกับ loop for
for item in range(len(tup)):
    print(tup[item])

#การสร้างและเพิ่มข้อมูล(join)
x=("Pp")
print(type(x)) #Program จะมอง x เป็น string
x=("Pp",)
print(type(x)) #Program จะมองเป็น tuple
name=("PPP","Kop")
new=("nut",)
name=name+new
print(name)

#การทำงานร่วมกับ list
lis=list(tup)
print(lis)
lis[1]="BKK"
tup = tuple(lis)
print(tup)

#การลบข้อมูล
tup = (1,2,3,4,"PP")
lis=list(tup)
print(lis) 
lis.remove(4)
tup=tuple(lis)
print(tup)

#การค้นหาและนับจำนวนสมาชิก count
x = tup.count(3) #ค้นเลข4 แล้วนับว่ามีอยู่กี่แห่ง
print(x)

#การค้นหาสมาชิกด้วย index
x=tup.index(1) #เช็คเจอเลข1ที่ index เท่าไหร่
print(x)

#การ sort ข้อมูล 
tup=(100,99,81,2,3)
print("Before :",tup)
lis=list(tup)
lis.sort() #หรือจะreverseก็ได้ lis.reverse()
tup=tuple(lis)
print("After:",tup)
