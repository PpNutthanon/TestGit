#Random Module
import random 
for i in range(10):
    x=random.random() #Range จะอยู่ระหว่าง 0.0 - 1.0
    print(x)

for i in range(10):
    y=random.uniform(5,10) #สุ่มตัวเลขช่วง 5 จนถึงก่อน 10
    print(y)

for i in range(10):
    z=random.randrange(1,10,2) #สุ่มตัวเลข 1-10 โดยขยับทีละ2(จะมีแค่ 1 3 5 7 9)
    print(z)

for i in range(5):
    a=random.randint(1,5) # สุ่มตัวเลข 1 ถึง 5(รวมเลข5ด้วย)
    print(z)

item=[1,2,3,4,5,"Pp","BKK"]
b=random.choice(item) #สุ่มหยิบสมาชิกใน item
print(b)
for i in range(5):
    c=random.shuffle(item) #สุ่มสลับตำแหน่งสมาชิกใน item
    print(c)

for i in range(15):
    d=random.choice("123456") #สุ่มมาหนึ่งตัว
    print(d)