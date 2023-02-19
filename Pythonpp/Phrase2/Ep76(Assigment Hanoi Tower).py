#Assignment หอคอยฮานอย
'''
n= จำนวนจาน 
เสา => A B C
มีจานจำนวน 3 ใบ
n=1
n=2 (n-1)
n=3 (ใหญ่สุด)
'''
# A=> ล ก ญ
#A ล ก => B
#C => ? ? ?
def hanoi(n,a,b,c): #จำนวนจาน,จุดย้าย,จุดพัก,จุดไป
    # a=> c
    if n==0:
        return
    hanoi(n-1,a,c,b) #ย้าย a(เล็กกับกลาง)ไปใส่ที่ b โดยให้ c เป็นจุดพัก
    print("Plate",n,"From",a,"To",c)
    hanoi(n-1,b,a,c)
hanoi(3,"A","B","C")