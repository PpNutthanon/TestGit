# foreground => สีของตัวอักษร
from tkinter import *
def Hello():
    print("Hello World")

mainWindow = Tk()

button = Button(mainWindow, text = "Click Me1!", command = Hello,width=20,height=10).grid(row=2,column=1)
button2 = Button(mainWindow, text = "Click Me2!", command = Hello).grid(row=1,column=1) #? เพิ่มค่าแกน Y จะลงมาข้างล่างแทน(ขัดกับหลักคณิตศาสตร์นิดนึง)
button3 = Button(mainWindow, text = "Click Me3!", command = Hello,fg="magenta",bg="blue",highlightcolor="yellow",highlightbackground="green").grid(row=1,column=2)
label = Label(mainWindow, text = "Hello World",width=20,fg="red",bg="black").grid(row=0,column=1)


mainWindow.mainloop() #Todo แสดงหน้าจอเปล่า

'''
activebackground - Background color for the widget when the widget is active.

activeforeground - Foreground color for the widget when the widget is active.

background - Background color for the widget. This can also be represented as bg.

disabledforeground - Foreground color for the widget when the widget is disabled.

foreground - Foreground color for the widget. This can also be represented as fg.

highlightbackground - Background color of the highlight region when the widget has focus.

highlightcolor - Foreground color of the highlight region when the widget has focus.

selectbackground - Background color for the selected items of the widget.

selectforeground - Foreground color for the selected items of the widget.
'''