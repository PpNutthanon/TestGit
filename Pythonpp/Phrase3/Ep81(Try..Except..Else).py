#Try...Except...Else
try:
    a=float(input("Enter The First Number :"))
    b=float(input("Enter The Second Number :"))
    result=a/b
    print("The Result Is :",a/b)
except Exception as problem:
    print("The Program Error Because :",problem)
else:#จะทำงานก็ต่อเมื่อไม่มีข้อผิดพลาด(ไม่พบExceptionในโปรแกรม)
    print("Finish Program")