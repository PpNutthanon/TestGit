#Arbitary Arguments
#แบบปกติ
def displaydata(fname):
    print(fname)
displaydata("PP")
displaydata(fname="Nutthanon")

#*args => ค่าใน parameter มีได้หลายค่า จะเป็นtuple
def add(*number):
    sum=0
    for i in range(len(number)):
        sum+=number[i]
    print(sum)

#**kwarg => ชื่อ parameter มีได้หลายชื่อ จะเป็นdictionary
def displayinfo(**kwargs): #สามารถเปลี่ยนชื่อ kwargs ได้ แค่อย่าลืมใส่ ** นำหน้า
    print(kwargs)
    #print(kwargs)["fname"] => ให้แสดงเฉพาะ fname
displayinfo(fname="PP",lname="Nutthanon",city="BKK")
displayinfo(lname="Timming",age=19,status="Single")
displayinfo(singlename="GG",sport="Football")
displayinfo(country="England")

