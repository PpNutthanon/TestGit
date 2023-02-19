#Control Structure
'''
1) แบบลำดับ (บนลงล่าง ซ้ายไปขวา)
2) แบบเลือก (if else)
3) แบบทำซ้ำ (for while)

if boolean expression: #เงื่อนไขต้องเป็นจริงถึงทำงานต่อได้
   statement 
'''
name = input("Enter your name :")
age = int(input("Enter your age :"))
print(type(name=="pp"))
print(type(age == 15))
if age>=15:
    print("สวัสดี นาย " + name +" คุณมีอายุ",age)
    print("Thank for using program") #ถ้าอายุน้อยกว่า15 จะไม่runตรงนี้ เพราะคำสั่งนี้อยู่ภายใต้เงื่อนไข if
#if condition:

