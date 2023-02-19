#กำหนดคุณสมบัติกราฟแท่ง
import matplotlib.pyplot as plt
course = ["Python","Java","C#"]
score = [80,75,50]
c = ["green","orange","blue"] #? กำหนดสีของอต่ละแท่ง
#width => กำหนดขนาดของ Bar, edgecolor=เส้นขอบ, linewidth=ความหนาของเส้นขอบของBar
plt.bar(course,score,color=c,width=0.6,edgecolor="yellow",linewidth=3) 
#*Todo ถ้าอยากให้แสดงแนวนอน => plt.barh() แต่ต้องระวังเพราะแกนจะสลับกัน(ต้องปรับใหม่)
plt.show()