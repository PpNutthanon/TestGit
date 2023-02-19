#การเขียนลดรูป Exception
try:
    a=float(input("Enter The First Number :"))
    b=float(input("Enter The Second Number :"))
    result=a/b
    print("The Result Of Addition Is :",result)
except Exception as e: #โปรแกรมจะบอกว่าผิดเพราะอะไร
    print("Program Error Because :",e)