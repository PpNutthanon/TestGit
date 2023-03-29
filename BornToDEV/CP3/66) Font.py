# W => ซ้ายมือ
# E => ขวามือ
from tkinter import *
main=Tk()
text1 = Label(main,text="Hello World",width=20,fg="red",bg="black",font=("Helvetica",40),anchor=W).grid(row=0) 

text2 = Label(main,text="Hello Pp",width=20,fg="Yellow",bg="Magenta",font=("Helvetica",40),anchor=E).grid(row=0,column=1) 
main.mainloop()