#List ข้อมูลในlistจะเรียกว่า สมาชิก
#เก็บ booleans string number ... ได้
# (เก็บข้อมูลต่างชนิดในlistเดียวกันก็ได้)

#Primitive
a,b,c,d,e=1,2,3,4,5
print(a,b,c,d,e)
#NonPrimitive
number = [] #listว่าง
number = [1,2] #list มีสมาชิก 1,2
name=["PP","G","T"] #list name มีสมาชิกเป็นข้อความ
all = [10,"PPP",True,3.14,-10] #เก็บค่าต่างชนิดกันได้

#แสดงผล
print(name)
print(type(name))



#Constructor
pop = list(["A","B","C"])#การประกาศแบบconstructor

#การเข้าถึงข้อมูลlist
print(pop[0]+name[0])
print(all[2])
print(all[-3]) #ไล่จากข้างหลังมาข้างหน้า

#การเข้าถึงข้อมูลแบบกำหนดช่วง
print(all[0:3]) #เริ่มจาก0จนถึง2
print(all[-4:-1])
print(all[2:]) #เริ่มจาก2ไปจนถึงตัวสุดท้าย

#การแก้ไขข้อมูล
#ชื่อตัวแปร [index] = "ข้อมูลที่แก้ไข"
a=list([1,2,3,4,5,6,])
print(a) #ก่อนแก้ไข
a[2]= 9 #แก้ตำแหน่งที่2(เลข3) ไปเป็นเลข 93
print(a) #หลังแก้ไข
a[-1]=0
print(a)

#การแสดงผลด้วย loop
sum=0
for x in a:
    print("Member of a is",x)
    sum+=x #sum = sum+x
print("Summation is",sum)

#การตรวจสอบข้อมูล
fruit=["mango","orange","banana"]
b=[1,2,3]
if "mango" in fruit:
    print("mango is the member")
else:
    print("mango is not the member")
if 0 in b:
    print("0 is in the b")
else:
    print("0 is not in the b")


#การนับจำนวนสมาชิก
print(len(fruit)) #มี3ตัว แต่ตำแหน่งนับแบบ 0,1,2
for i in range(len(fruit)):
    print(fruit[i])
for item in fruit:
    print(item) #ผลลัพธ์เหมือนบรรทัดที่ 64 65

#การเพิ่มข้อมูล 
# append(เอาข้อมูลมาต่อท้าย) 
# insert(การแทรกข้อมูลเข้าไป)
# ชื่อlist.append("ตัวที่จะเพิ่ม")
# ชื่อlist.insert (index,ตัวที่จะเพิ่ม)
print(fruit) #ก่อนเพิ่มข้อมูล
fruit.append("watermelon")
print(fruit) #หลังเพิ่มข้อมูล
fruit.insert (1,"durian") #เพิ่มdurianให้ไปแทรกที่ indexที่1
print(fruit)
print("\n")

#การลบข้อมูล remove,pop,del,clear
# ชื่อlist.remove("ชื่อที่จะลบ")
# pop => เอาตัวหลังสุดของlistออก
# ชื่อlist.pop()
# del=delete(การลบแบบระบุindex)
# del ชื่อlist[indexที่จะลบ]
# clear => ล้างข้อมูลสมาชิกทั้งหมดของlist
# ชื่อlist.clear()
print(fruit) #ก่อนremove
fruit.remove("banana")
print(fruit) #หลัง remove

fruit.pop() #ลบตัวสุดท้ายออก
print(fruit) 
del fruit[1] #ลบindexที่1ออก
print(fruit)
fruit.clear() #ลบสมาชิกออกหมด
print(fruit)

#การคัดลอกข้อมูล
#ตัวที่จะวางข้อมูลลงไป  = ตัวที่คัดลอก.copy()
c = [1,2,3,4,5]
y=[]
print(y)
y = c.copy()  #คัดลอกข้อมูลcมาใส้ในy
print(y)

#การรวมข้อมูลของlist
allgroup = number+c
print(allgroup)

#การแสดงจำนวนสมาชิก(count)
#ชื่อlist.count("ข้อมูลที่ต้องการจะนับ")
z = allgroup.count(2) #นับว่าในallgroup มี2กี่ตัวในlist
print(z)

#extend
# ชื่อlist.extend(ชื่อlistที่จะเพิ่ม)