#ทำตารางหมากฮอส 

for i in range(1,9):
    for j in range(1,9):
        if (i+j)%2==0:
            print("x",end='')
        else:
            print("o",end='') 
#บรรทัดที่ 5-8 เขียนแบบ ternary จะได้เป็น
# print("x",end='') if (i+j)%2==0 else print("o",end='')
        
    print("\n")