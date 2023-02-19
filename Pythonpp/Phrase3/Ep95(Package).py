#Package => จัดกลุ่ม module ให้อยู่ตำแหน่งเดียวกัน
#สิ่งสำคัญคือกรอกที่อยู่ของ module ให้ถูกต้อง ไม่งั้นโปรแกรมจะหาไม่เจอ
from MyPackage.CalculateServices import addition #ถ้าพิม import CalculateServices โปรแกรมจะหาไฟล์ไม่เจอ
from MyPackage.Weather import city as ct
print(ct)
addition(10,50)

