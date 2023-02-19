#Control Structure (for loop)
'''
for => รู้จำนวนรอบชัดเจน 
while => ไม่รู้จำนวนรอบที่ชัดเจน
'''
#for i in range(start,stop,step) #กำหนดรอบ#
#Program แสดง Hello World 3รอบ
summation = 0
for i in range(3): #range จะเริ่มต้นที่ 0,1,2(ทำงานก่อนถึงเลข3)
    summation+=i
    print("รอบที่",i,"sum",summation)
print(summation)
print("\n")
for i in range(1,5):#ทำงานรอบที่ 1 ถึง 4
    print("Round",i,"PP")
print("\n")
for i in range(1,6,2):#เริ่มที่1จบที่5เพิ่มทีละ2
    print("Round",i,"WTF")
for i in range(-10,5): #รอบติดลบได้
    print("Round =",i)
for i in range(10,0,-1): #ลดค่าได้
    print("รอบบ",i)

    

