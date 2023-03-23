try:
    a = int(input("Enter Number: "))
    b = int(input("Enter Number: "))
    print(a/b)
except ValueError:
    print("Error Can Input Only Number")
except ZeroDivisionError:
    print("Error You Can't Enter Zero in Denominator")
except:
    print("Error")