#Program Calculate BMI แบบดีกว่าเดิม
'''
<18 ต่ำกว่าเกณฑ์
18.5 -22.9 = สมส่วน
23.0 - 24.9 = น้ำหนักเกิน
25.0 - 29.9 = โรคอ้วนปกติ
>30 = โรคอ้วนระดับอันตราย
'''

weight = float(input("Enter your weight(kg) :"))
height = float(input("Enter your height(cm) :"))/100
BMI = weight/(height**2)
print("Your Body Mass Index(BMI) is :",BMI)
if BMI>=0 and BMI<=18:
    print("Your body is below the standard")
elif BMI>18 and BMI<23:
    print("Your body is standard")
elif BMI>=23 and BMI<25:
    print("Your body is overweight")
elif BMI>=25 and BMI<30:
    print("Your body is normal obesity")
else:
    print("Your body is dangerous obesity")
print("Thank you for using program")

#เขียนได้อีกวิธี(แบบสมบูรณ์กว่า)
weight = float(input("Enter your weight(kg) :"))
height = float(input("Enter your height(cm) :"))/100
BMI = weight/(height**2)
print("Your Body Mass Index(BMI) is : ",BMI)
result = "The Program is error"
if BMI>0 and BMI<18.5:
    result = "You are thin"
elif BMI>=18.5 and BMI<23:
    result = "You are fit"
elif BMI>=23 and BMI<25:
    result = "You are overweight"
elif BMI>=25 and BMI<30:
    result = "You are obesity level 1"
elif BMI>=30:
    result = "You are obesity level 2"
print(result)

