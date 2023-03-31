# การเขียนโปรแกรมเชิงวัตถุ
#? Class => แบบแปลนของวัตถุ 
#? ภายใน Class จะมี Attribute(คุณลักษณะ, ตัวแปร) และ Behavior(พฤติกรรม, function การทำงาน) อยู่ภายใน
#Todo object => ผลลัพธ์ ที่เรียกใช้งานจาก Class

class Customer: #Class
    name = "" #Attribute
    lastname = "" #Attribute
    age = 0
    
    def addcart(self,):
        print("Added to Cart",self.name,self.lastname,self.age)

customer1  = Customer() #Object
customer1.name = "Nutthanon"
customer1.lastname = "Hwungsawart"
customer1.age = 21

customer2  = Customer() #Object
customer2.name = "Much"
customer2.lastname = "Chanatip"
customer2.age = 20

customer3  = Customer() #Object
customer3.name = "Sine"
customer3.lastname = "Apatcha"
customer3.age = 23

customer4  = Customer() #Object
customer4.name = "Pun"
customer4.lastname = "Warinthon"
customer4.age = 21

customer = [customer1, customer2, customer3, customer4]

for customer in customer:
    customer.addcart()
