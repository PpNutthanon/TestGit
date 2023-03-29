from tkinter import *

def leftclick(event):
    print("Left Click")

def doubleclick(event):
    print("Double Click")

main = Tk()
button = Button(main, text="My Button", width=10, fg="White", bg="Black", font=("Didot", 10))
button.pack()
button.bind("<Button-1>", leftclick)
button.bind("<Double-1>", doubleclick)

main.mainloop()

#TODO More Function About Event-Driven : https://python-course.eu/tkinter/events-and-binds-in-tkinter.php