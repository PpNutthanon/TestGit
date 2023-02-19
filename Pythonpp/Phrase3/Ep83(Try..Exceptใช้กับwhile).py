#Try..Except ใช้น่วมกับ while
while True:
    try:
        a=float(input("Enter The First Number :"))
        b=float(input("Enter The Second Number :"))
        if a==0 and b==0:
            break
        result=a/b
        print("The Result Is :",result)
    except ValueError:
        print("Please Enter The Number")
    except ZeroDivisionError:
        print("Cannot Divided By Zero")
    finally:
        print("In Progressing")
    