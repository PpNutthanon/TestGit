#จัดการ Exception หลายเหตุการณ์
try:
    a=int(input("Enter The First Number :"))
    b=int(input("Enter The Second Number :"))
    result=a/b 
    print("The Answer Of Division Is :",a/b)
#มีข้อผิดพลาด 2 case
# 1) input ที่รับเข้ามาไม่ใช่ int(ValueError)
# 2) ส่วนเป็น 0
except ValueError:#ValueError เป็น BuildIn ฟังก์ชัน
    print("Must Be Input The Integer Only")
except ZeroDivisionError: #ZeroDivisionError เป็น BulidIn ฟังก์ชัน
    print("Can't Division By Zero")
except TypeError:
    pass #เช่น score= 19 +"PP"  