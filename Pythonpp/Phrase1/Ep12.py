#โปรแกรมคำนวณค่า BMI(ดัชนีมวลกาย)
#BMI = น้ำหนัก(kg)/ส่วนสูง**2 (m)
weight = float(input("Enter your weight(kg) :"))
height = float(input("Enter your height(cm) :"))
height/=100
BMI = weight/(height**2)
print("Your Body Mass Index(BMI) is :",BMI)
