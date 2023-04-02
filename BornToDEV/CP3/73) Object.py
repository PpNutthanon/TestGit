class Person:
    skin_color = ""
    hair = ""
    gender = ""
    age = 0
    def sayHello(self):
        print("Hello Mate!")
    def move(self):
        print("Moving!")

class Teacher(Person):
    def sayHello(self):
        print("Hello I'm teacher!")
    def teach(self):
        print("I'm going to teach you")

class Chef(Person):
    def sayHello(self):
        print("Hello I'm Chef!")
    def cook(self):
        print("Which menu do you prefer")

class Doctor(Person):
    def sayHello(self):
        print("Hello I'm Doctor!")
    def teach(self):
        print("What's your symtom")
        
alice = Person()
alice.skin_color = "white"
alice.hair = "short"
alice.gender = "Female"
alice.age = 28

Inheritance = Teacher()
Inheritance.skin_color = "white"
Inheritance.hair = "short"
Inheritance.gender = "Female"
Inheritance.age = 28
