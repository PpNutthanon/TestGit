#กราฟวงกลม => ส่วนใหญ่จะใช้แสดงสัดส่วนรวมกันให้ได้100%, ใช้แสดงเน้นส่วนที่สนใจเป็นพิเศษ
#? Structures => plt.pie(data,labels=lang)
#*Todo data=[15,30,45,60,40]
#*Todo lang=["PHP","Flutter","Nodejs","C#","JavaScript"]
#* autopct="%.1f%%" => ให้แสดงพื้นที่เป็นจำนวนเปอร์เซ็นต์
import matplotlib.pyplot as plt
student = [10,20,40,30,60]
course = ["PHP","JavaScript","Python","C#","Nodejs"] #! Course กับ Data ต้องมีจำนวนสมาชิกเท่ากัน
plt.pie(student,labels=course,autopct="%.1f%%")
plt.show()