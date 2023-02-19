#Set Operator
fruit1={"Mango","Banana","PassionFruit","Lychie","Apple"}
fruit2={"Watermelon","Durian","Strawberry","Orange","Apple"}

#Union
allfruit=fruit1.union(fruit2)
print(allfruit)
fruit1.update(fruit2)
print(fruit1) #ทำแบบบรรทัดที่6หรือ8ก็ได้

#Copy Set
fruitc={} 
friutc=fruit1.copy() #Copyfruit1 มาในc
print(fruit1) 

#Refference
a=fruit1.difference(fruit2) #เอา 1-2
print(a)

#Intersection
b=fruit1.intersection(fruit2) #fruit1 intersec fruit2
print(b)

#Subset
fish={"ปลาดุก","ปลาโลมา","ปลาฉลาม"}
x={"ปลาหมอ","ปลาเสือ"}
y={"ปลาดุก"}
print(x.issubset(fish)) #xเป็นsubsetของfishมั้ย
print(y.issubset(fish))

#Superset
print(fish.issuperset(x)) #xอยู่ในfishมั้ย
print(fish.issuperset(y))

#หาค่าmin max ใน set
number = {2,34,-10,0,987,12.21}
print(min(number))
print(max(number))