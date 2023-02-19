#Slice Array 1มิติ
#Structure => name[start:end]
import numpy as np
a=np.arange(1,11)
print(a)
print(a[2])
print(a[:]) #เหมือนกับปริ้น a
print(a[2:]) #ตั้งแต่ index ที่2 จนถึง index สุดท้าย
print(a[7:]) #ตั้งแต่เลข 8 เป็นต้นไป จนถึงตัวสุดท้าย
print(a[:5]) #นับตั้งแต่ index0-index4
print(a[2:9:2])

b=np.array([20,10,30,50,40])
print(b[1:])
print(b[1:4])
print(b[1:4:2]) #กระโดดข้ามสมาชิกไป 2 ตัว

c=np.array([10,30,40,50,60,70,75,90])
print(c[::2])
print(c[::3])
