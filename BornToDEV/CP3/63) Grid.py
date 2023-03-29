# GUI => Graphic User Interface
# tkinter => function จัดการ User Interface 
# Widget => สิ่งต่างๆที่เห็นอยู่ในฟอร์มของโปรแกรม
from tkinter import *
def Hello():
    print("Hello World")

mainWindow = Tk()

button = Button(mainWindow, text = "Click Me1!", command = Hello).grid(row=0,column=1)
button2 = Button(mainWindow, text = "Click Me2!", command = Hello).grid(row=1,column=1) #? เพิ่มค่าแกน Y จะลงมาข้างล่างแทน(ขัดกับหลักคณิตศาสตร์นิดนึง)
button3 = Button(mainWindow, text = "Click Me3!", command = Hello).grid(row=1,column=2)


mainWindow.mainloop() #Todo แสดงหน้าจอเปล่า