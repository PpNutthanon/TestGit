#Try...Except
'''
try:
    คำสั่ง run program ปกติ
except:
    คำสั่งที่ทำงานตอนโปรแกรมมีข้อผิดพลาด
'''
try:
    number1=int(input("Enter The First Number :"))
    number2=int(input("Enter The Second Number :"))
    result=number1/number2 #Exception มี 2 อย่าง คือ กรอกข้อมูลที่ไม่ใช่ int กับ ส่วนมีค่าเท่ากับ0
    print(result)
except:
    print("The Program Is Error")