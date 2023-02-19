#ตัวเลขขั้นบันได
'''
input = 3
1
2
123
'''
number = int(input("Enter the number :"))
for row in range(1,number+1):
    for column in range(1,row+1):
        print(column,end='') #end คือออะไร
    print("\n")
'''
input = 3

row = 1
column = 1,2
1

row = 2
column = 1,3
12

row = 3
column = 1,4
123
'''