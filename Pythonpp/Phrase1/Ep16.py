#เงื่อนไขแบบ if ซ้อน if
age = int(input("Enter your age :"))
if age<=15:
    if age==15:
        print("You study level 9")
    elif age == 14:
        print("You study in level 8")
    elif age ==13:
        print("You study in level 7")
    else:
        print("You study in primary school")
    
    
else:
    print("You study in High School")
print("Thank you for using program")
