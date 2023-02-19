#ฟังก์ชัน เรียก ฟังก์ชัน
def compare(x,y):
    if x>y:
       return x
    else:
        return y

max=compare(10,20)
print("Maximum value is",max)

def equal(x,y,z):
    #ฟังก์ชันเรียกฟังก์ชัน
    a = compare(x,y)
    m = compare(a,z)
    return m
me=equal(10,20,30)
print(me)
def displaycity():
    print("Hello BKK")
def displayfood():
    displaycity()
    print("Bacon")
displayfood()



