# Capitalize => ทำให้ตัว String ข้างหน้าสุดเป็นพิมพ์ใหญ่
firstname = input("Firstname: ").capitalize()
lastname = input("Lastname: ").capitalize()
print("Hello %s %s" %(firstname,lastname))

# Center => ทำให้ข้อความอยู่ตรงกลาง
# len => ตรวจสอบว่าข้อความมีทั้งหมดกี่ตัว
text= "Nutthanon"
textformat = "Welcome %s"%(text)
print(textformat.center(25,"-"))
print(len(firstname))
