# GUI => Graphic User Interface
# tkinter => function จัดการ User Interface 
# Widget => สิ่งต่างๆที่เห็นอยู่ในฟอร์มของโปรแกรม
from tkinter import *
def Hello():
    print("Hello World")

mainWindow = Tk()
button = Button(mainWindow, text = "Click Me!", command = Hello)
button.place(x=50,y=20)
mainWindow.mainloop() #Todo แสดงหน้าจอเปล่า

mainWindow2 = Tk()
button2 = Button(mainWindow2, text = "Click Me!", command = Hello)
button2.place(x=50,y=50)
mainWindow2.mainloop()
