# ฮิสโทรแกรม(Histogram) => แสดงความถี่ของข้อมูล(ส่วนใหญ่ใช้กับการหาช่วงของข้อมูล) => plt.hist(ค่าที่ต้องการ)
import matplotlib.pyplot as plt
age=[18,17,20,18,20,15,19,20,17,16,15,14,16,17,20]
plt.hist(age)
plt.xlabel("Age",size=20), plt.ylabel("Amount",size=20)
plt.title("Total Age",loc='center')
plt.show()