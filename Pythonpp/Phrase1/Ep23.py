#เจาะลึกstring part1
name = "Nutthanon Pp Pp" #index=ช่องของตัวอักษรที่อยู่ในข้อความนั้นๆ
a = " guitar "

#การเข้าถึงตัวอักษรใน string(index)
print(name)
print(name[0]) #index จะเริมต้นที่0
print(name[0:3]) #จะได้Nut, 0:3คือเริ่มที่0แล้วจบที่2
print(name[:3]) #จะแสดงผลเหมือนบรรทัดที่5
print(name[0:11]) #ช่องว่างก็นับเป็น index
print(name[-3:]) #ขยับจากข้างหลังมา

#len function(หาว่าข้อความมีกี่ตัว)
print(len(name)) #ดูว่ามีกี่ตัว(program runว่ามี15ตัว คือ 0ถึง14)
print(len(a)) #ช่องว่างตอนแรก

#ลบช่องว่าง(ทั้งหมด,ซ้าย,ขวา) strip
a = a.strip() #ทำให้ช่องว่างทั้งหมด
a = a.lstrip() #ลบช่องว่างด้านซ้าย
a = a.rstrip() #ลบช่องว่างด้านขวา
print(len(a)) #ช่องว่างหลังลบออกแล้ว

#แปลงพิมใหญ่ พิมเล็ก
print(name.upper()) #แปลงพิมเล็ก => พิมใหญ่ ทั้งหมด
print(name.lower()) #แปลงพิมใหญ่ => พิมเล็ก ทั้งหมด
print(a.capitalize()) #ให้ตัวหน้าเป็นตัวพิมพ์ใหญ๋

#การแทนที่ตัวอักษรด้วย ตัวอักษรอื่น
print(name.replace("Nutthanon","555")) #แทนที่Nutthanon เป็น555
print(name.replace("Pp","3.5"))
print(name.replace("Pp","timming",1))#replace แค่ตัวแรก
print(name.replace("Pp","timming",2))#replaceสองตัวเลย(เหมือนบรรทัด24)

#การเช็คข้อความ => True,False
x = "Nutt" in name
y = "op" in name
print(x,y) #เช็คว่าคำนี้อยู่ในตัวแปร name มั้ย
if x:
    name = name.replace("Nutt","Wwe")
print(name)
