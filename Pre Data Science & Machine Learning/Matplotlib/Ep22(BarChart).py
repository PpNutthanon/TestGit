#กราฟแท่ง(Bar Chart) => plt.bar()
import matplotlib.pyplot as plt
course = ["Python","Java","C#"]
score = [80,75,50]
plt.bar(course,score,color="green")
plt.title("The Score Subject You Enroll")
plt.xlabel("Course"), plt.ylabel("Score")
plt.show()