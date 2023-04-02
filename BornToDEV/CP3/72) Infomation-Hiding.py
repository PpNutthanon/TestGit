# Information Hiding => การปกปิดข้อมูล
# Encapsulation =>  __
# Getter => ฟังก์ชันที่จะดึงออกมาตรงๆ
# Setter => ฟังก์ชันในการกำหนดค่า
class Animal():
    def eat(self):
        print("Eating Eating!")

class Cat(Animal):
    __name = ""
    def setname(self,text):
        self.name = text
        print("Setting name = ",self.name)

    def eat(self):
        print("Meow",self.name)

cat1 = Cat()
cat1.setname("Nutthanon")
cat1.eat() 
animal1 = Animal()
animal1.eat()