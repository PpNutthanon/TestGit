# Tuple => เหมือน list แต่ ไม่สามารถเปลี่ยนแปลงแก้ไขค่าต่างๆได้ (เหมาะกับการใช้เก็บข้อมูลที่ไม่ได้เปลี่ยนแปลงบ่อยๆ)
tuple1 = ("Prame","Pp","Much")
print(tuple1,type(tuple1))
tuple2 = ("Bank","A")
tuple3 = tuple1 + tuple2
print(tuple3)
print(tuple3[1:])
print(tuple3[:2])
print(tuple3*2)
print("Pp" in tuple3)
print("TER" in tuple3)

for i in tuple3:
    print("Hello",i)