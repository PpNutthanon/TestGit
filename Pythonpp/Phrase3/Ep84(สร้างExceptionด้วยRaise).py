#สร้าง Exception ด้วย Raise
while True:
    try:
        name=input("Enter Your Name :")
        a=float(input("ENter The Number :"))
        b=float(input("ENter The Number :"))
        if a==0 and b==0:
            break
        if a<0 or b<0:
            raise Exception("Cant Input Negative Value")
        if name=="Pp":
            raise Exception("Have In Account")
        result=a/b
        print("The Result is :",result)
    except Exception as problem:
        print("The Program Error Because :",problem)

