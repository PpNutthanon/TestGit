#List Tuple
lis=["Red","Yellow","Green"]
tup=("Red","Yellow","Green")
print(lis[0])
print(tup[0])

#Dictionary => key(การเข้าถึงข้อมูล),value(ค่าของข้อมูล)
#list,tuple => index,value

#การสร้าง dictionary => ทั่วไป,constructor
#ชื่อตัวแปร={key:value,key:value,key:value}
#ใส่keyซ้ำกันไม่ได้ ถ้าซ้ำจะได้เป็นkeyล่าสุดที่ใส่เข้าไป

#แบบทั่วไป
color={"Red":"สีแแดง","Yellow":"สีเหลือง","Green":"สีเขียว",98:"บ้านแสนสุข"}
print(type(color))
print(color["Red"]) #โปรแกรมจะแสดง สีแดง
print(color["Yellow"])
print(color[98])

city={"กรุงเทพ":"Bangkok"}
print(city["กรุงเทพ"])
print(city.get("กรุงเทพ"))

student={"Kong":40,"PP":40}
print("The score of Kong is",student["Kong"])

dorm={300:"Pp",301:"Timmimg",302:"Copter"}
 
#แบบ Constructor
animal=dict(cat="แมว",dog="หมา",duck="น้องเป็ด")
print(animal["cat"])
print(animal.get("dog")) #แสดงผลได้เหมือนกัน

#การแก้ไขข้อมูล 
color={"Red":"สีแแดง","Yellow":"สีเหลือง","Green":"สีเขียว",98:"บ้านแสนสุข"}
color[98]="บ้านสวน" #แก้value ที่ key98 ให้เป็น บ้านสวน
print(color)

#การเพิ่มข้อมูล
color.update({"orange":"สีส้ม","violet":"สีม่วง "})
print(color)

#การวนloop
for item in color:
    print(item) #จะprint keyออกมาอย่างเดียว
#for item in color:
    #print(item.value)จะprint value อย่างเดียว

#การลบข้อมูล
print(color)
color.pop("Red") #ลบ Red ออกจาก color
print(color)

color.popitem() #ลบข้อมูลตัวสุดท้ายออก
print(color)

color.clear() #ลบข้อมูลออกทั้งหมด แต่เหลือ dictionary เปล่า
print(color)
#color.del() คือการลบcolorออกจากโปรแกรม

#การคัดลอก Dictionary 
x=color.copy() #ลอก color ลงใน x
print(x)


#Dictionary แบบหลายข้อมูลในอันเดียว
market={
    "Coco":{
         "name":"PP",
         "menu":["Curry","Noodles"],
         "zone":"North East"
    },
    "MK":{
        "name":"KK",
        "menu":["Mango","Durian"],
        "zone":"North"
    },
    "Peper Lunch":{
        "name":"A",
        "menu":["Coke","Pepsi"],
        "zone":"South"
    }
}
print(market)
print(market["Coco"])
print(market["Coco"]["menu"])

#Check Dictionary
if "Noodles" in market["Coco"]["menu"]:
    print(True)
else:
    print(False)