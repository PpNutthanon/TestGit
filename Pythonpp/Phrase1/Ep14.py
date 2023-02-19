#If else condition
'''
if จริง :
    ทำอะไร
else :
    ทำอะไร
'''

name = input("Enter your name :")
age = int(input("Enter your age :"))
if age >= 15:
    print("สวัสดี นาย "+ name)
    print("คุณมีอายุ",age)
else:
    print("สวัสดี เด็กชาย "+name)
    print("คุณมีอายุ",age)  
print("Thank you for using program")

'''
age = int(input("Enter your age")) #if จะทำการเช็คทุกกรณี
if age>=15:
    print("Hello Teenager")
elif age>=20:  #elif ถ้าจริงแล้วจะตัดจบทันที
    print("Hello Adult")
elif age>=30:
    print("Hello working man")
else:
    print("Hello Children")
print("Thak you for using program") #โปรแกรมยังไม่สมบูรณ์
'''
#ต้องกำหนด 15-20=>วัยรุ่น 21-60=>วัยทำงาน >60 =>วัยเกษียณ
#ใช้ and or not เพื่อช่วยให้เขียนง่ายขึ้น
#โปรแกรมสมบูรณ์
age = int(input("Enter your age :"))
if age>=15 and age<=20:
    print("Hello Teenager")
elif age>=21 and age<=60:
    print("Hello Working")
elif age>60:
    print("Hello Retire")
else:
    print("Hello Kids")
print("Thank for using program")
