# Overriding => Class ลูกที่ไปสืบทอดมีการทำงานที่แตกต่างจาก Class แม่ เราสามารถเขียนการทำงานทับได้แต่จะต้องชื่อเดียวกัน
class Animal:
    def eat(self):
        print("Eating Eating!")

class Cat(Animal):
    def eat(self):
        print("Meow")       

cat1 = Cat()
cat1.eat()
animal1 = Animal()
animal1.eat()
