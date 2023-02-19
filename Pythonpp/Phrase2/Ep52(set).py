# set => สมาชิกซ้ำกันไม่ได้
'''
list=[] ข้อมูลต่างชนิดกันได้, แก้ไขข้อมูลสมาชิกได้ , ข้อมูลซ้ำกันได้,ซ้ายไปขวา
tuple=() ข้อมูลต่างชนิดกันได้ , แก้ไขข้อมูลสมาชิกไม่ได้ , ข้อมูลซ้ำกันได้ , ซ้ายไปขวา
set={} ข้อมูลต่างชนิดกันได้ , แก้ไขข้อมูลสมาชิกไม่ได้ , ข้อมูลซ้ำกันไม่ได้ , ลำดับไม่แน่นอน
'''
#แบบปกติ
fruit={"mango","banana","watermelon"}
print(fruit) #มีลำดับที่ไม่แน่นอน
print(type(fruit))

#แบบ Constructor
a=set(["Fish","Monkey","Dog"])
print(a)
print(type(a))
lis=["Cat"]
b=set(lis) #เปลี่ยน list เป็น set
print(b)

number={1,1,2,3,4,5,6}
print(number) #set จะไม่นับตัวซ้ำ

#การเพิ่มข้อมูลสมาชิกทีละตัว
number.add(10) #เพิ่ม10ไปในset number
print(number)
a.add("octopus")
print(a)

#การเพิ่มข้อมูลสมาชิกหลายๆตัว
b=["Yellow","Red","Brown","Violet"]
fruit.update(b) #เพิ่ม list b ไปใน fruit
print(fruit)

#การแสดงผลโดยการใช้ loop
for item in fruit:
    print("ข้อมูล =>",item)

#การเช็คจำนวนสมาชิกในเซต
print(len(fruit))

#การเช็คข้อมูลในเซ็ต
if "Yellow" in fruit:
    print("Yes it have")
else:
    print("No it doesn't")

print("red" in fruit)

#การลบข้อมูลสมาชิกในเซต
#remove,discard 
fruit.remove("mango") #ลบ mango ออกจาก fruit
print(fruit)
fruit.discard("KKK")
print(fruit)
'''
จะremoveได้ต้องเป็นสมาชิกที่อยู่ในเซตเท่านั้น
discardไม่จำเป็นต้องเป็นสมาชิกที่อยู่ในเซต
'''

#การลบข้อมูลทั้งหมดในเซต
a.clear() #เอาสมาชิกออกทั้งหมดแต่ยังเหลือเซต
print(a)
del a #ลบ a ออกจากโปรแกรมเลย

