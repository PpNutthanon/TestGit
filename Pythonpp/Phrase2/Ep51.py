#นำค่าใน tuple => ตัวแปร
tup=(10,20,30)
a,b,c=tup #ให้a=10.b=20,c=30
print(a)
print(b)
d=a+c
print(d)

#สลับ tuple
x=(50,60)
y=(88,99)
print("Before")
print(x)
print(y)
x,y=y,x #สลับtuple x กับ y
print("After")
print(x)
print(y)

#tuple => string
character=("k","l","m")
name="".join(character)
print(name)

#reverse tuple
x=(100,20,30,15,500)
print(x)
x=list(x)
x.reverse()
x=tuple(x)
print(x)

#string => tuple
x="NUTTHANON"
y=tuple((x))
print(y)