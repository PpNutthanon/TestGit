#Stackbar/Stackplot
#? มีห้องเรียน3ห้อง => ในแต่ละห้องมีนักเรียน ชายหญิง => ให้แสดงอัตราส่วนผ่าน Stackbar(ชายกี่คน หญิงกี่คน)
import matplotlib.pyplot as plt
room = ["A","B","C"]
boy = [10,15,5]
girl = [20,7,15]

#*Todo สร้าง Bar ขึ้นมา 2 ก้อน
plt.bar(room,boy,label="Boy",color="blue")
plt.bar(room,girl,bottom=boy,label="Girl",color="orange") #* bottom=boy => นำข้อมูล Boy ไปอยู่ข้างล่าง Girl
plt.legend()
plt.show()

plt.stackplot(room,boy,girl,labels=["Boys","Girls"],colors=["green","pink"]) #! บอกเป็นพื้นที่
plt.legend()
plt.show()