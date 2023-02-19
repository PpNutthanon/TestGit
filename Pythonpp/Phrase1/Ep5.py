#Type Conversion (การแปลงชนิดข้อมูล)
x = 10
y = 3.8
z = "45.6"
a = "90"
#บวกเลข
result = x + y
print(result)
'''score = x + z 
print(score) #error เพราะชนิดข้อมูลแตกต่างกัน'''
#ต้องเปลี่ยน string => float ก่อน
score = x + float(z)
print(score)
#แปลง int => string
we = str(x) + z
print(we)
#แปลง string => int
pp = x + int(a)
print(pp)

print(int(y)) #จะปัดเลขลงตลอด
print(type(we))
print(type(x))
print(type(y))
z = float(z) #ทำแบบนี้จะสามารถนำค่าไปใช้งานต่อได้
print(type(z))