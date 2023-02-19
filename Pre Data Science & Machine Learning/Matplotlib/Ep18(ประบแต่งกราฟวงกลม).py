#ปรับแต่งกราฟวงกลม
import matplotlib.pyplot as plt
student=[10,20,40,30,60]
course=["PHP","Java","Python","C#","NodeJs"]

#? ปรับแต่งสีใหม่ และ Explode , startangle => ให้วงกลมหมุนไปกี่องศา
color=["purple","red","blue","yellow","green"]
exp = [0,0.2,0,0,0] # Explode => หยิบชิ้นส่วนที่(Java) 2ออกมาให้ห่างจากเดิม 0.2 => ยิ่งค่าเยอะยิ่งห่างมาก
plt.pie(student,labels=course,autopct="%.2f%%",colors=color,shadow=True,explode=exp,startangle=90) #*Todo Shadow คือ ให้กราฟเป็นเงาๆ
plt.show()

