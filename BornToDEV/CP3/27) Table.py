# Multiplication Table
start = int(input("Enter The Multiplication Table Start :"))
stop = int(input("Enter The Multiplication Table Stop :"))
for i in range(start,stop+1):
    print("Multiplication Table :",i)
    for j in range(1,13):
        print(i,"X",j,"=",i*j)


'''
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
2 x 11 = 22
2 x 12 = 24
'''