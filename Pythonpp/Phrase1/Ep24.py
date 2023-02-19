#เจาะลึกstring part2
first = "Nutthanon "
last = "Hwungsawart "
age = "19"
salary = 500.45

#การต่อstring
full = first + last + age
print(full)
print("firstname: "+first+"\tlastname:"+last+"\tage:"+age) #ยาว วุ่นวาย
text = "firstname:{0}\tlastname:{1}\tage:{2}"
print(text.format(first,last,age)) #สั้นกว่าแต่ผลลัพธืเหมือน บรรทัดที่8
text = "firstname:{1}\tlastname:{1}\tage:{2}"
print(text.format(first,last,age))
text = "firstname:{0}\tlastname:{1}\tage:{2}\tmonth:{3:.1f}"
print(text.format(first,last,age,salary))

#การนับจำนวนคำในประโยค
fruit = "ไปซื้อผลไม้ มีทุเรียน มังคุด กล้วย ส้ม ข้าวเหนียวทุเรียน ที่ตลาด"
print(fruit.count("ทุเรียน")) #นับว่ามีคำว่าทุเรียนกี่จุดในข้อความ

#การเช็คคำขึ้นต้น
b = "นายกอไก้ ใจดี"
print(b.startswith("นาย"))
if b.startswith("นาย"):
    print("Man")
else:
    print("Woman")

#การเช็คคำลงท้าย
c = "1150"
if c.endswith("50"):
    print("You won")
else:
    print("Next time")