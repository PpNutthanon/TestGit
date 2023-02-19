#Global Variable / Local Variable
def displaynumber():
    x=50 #ตัวแปรประเภท local
    print("Hello = ",x)

#โปรแกรมหลัก
x=20 #ตัวแปรประเภท global
displaynumber() #เรียกให้ฟังก์ชันแสดงผล
print("Hello = ",x)

#Global - ตัวแปรที่ทำงานทั้งโปรแกรม
#Local - ตัวแปรที่ทำงานเฉพาะส่วนนั้นๆ

