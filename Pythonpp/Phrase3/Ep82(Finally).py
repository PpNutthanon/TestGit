#Finally
try:
    a=float(input("Enter Number :"))
    b=float(input("Enter The Number :"))
    result=a/b
    print("The Result Is :",result)
except Exception as e:
    print("Program Error Because :",e)
finally: #โปรแกรม Run ได้หรือไม่ได้ ก็จะทำงาน
    print("Work On It")
#Finally ถ้าโปรแกรมทำงานไม่ได้ ก็จะแสดง
#Else ถ้าโปรแกรมทำงานไม่ได้ จะไม่แสดง