#เกมทายลูกเต๋า
#1,2,3,4,5,6 สุ่มตัวเลข แล้วให้ผู้ใช้เดาค่าที่สุ่ม 
'''
import random
i=1
a = random.randrange(1,7) #random number 1-6
print("You have 3 chance")
while True:
    number = int(input("Enter integer 1 to 6 :"))
    correct=(number==a)
    if not correct:
        if(number>correct):
            print("less than")
        if(number<correct):
            print("more than")

    if correct:
        print("You get 1 milion bath!")
        break
    if number<=0 or i==3:
        break
    i+=1
if not correct:
    print("Sorry play next time")
print("End of the program")
print("The number is",a)
'''
import random
i=0
pp = random.randrange(1,11)
print("You have 3 chance to enter the number 1-11")
while i<3:
    number = int(input("Enter the number :"))
    i+=1
    if number==pp:
        print("You're lucky!")
        break
    else:
        if number<pp:
            print("more than this")
        if number>pp:
            print("less than this")
        if i==3:
            print("Sorry play next time")
print("End of the program")
print("The number is",pp)

        


