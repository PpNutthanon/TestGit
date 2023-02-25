# Multiplication Table
start = int(input("Enter The Multiplication Table Start :"))
stop = int(input("Enter The Multiplication Table Stop :"))
for i in range(start,stop+1):
    print("Multiplication Table :",i)
    for j in range(1,13):
        print(i,"X",j,"=",i*j)