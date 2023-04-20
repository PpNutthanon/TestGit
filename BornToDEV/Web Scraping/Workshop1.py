from bs4 import BeautifulSoup
import requests
import pandas as pd
 
#ระบุตำแหน่งของเว็บปลายทาง
destination = requests.get("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")
soup = BeautifulSoup(destination.content, 'html.parser')


#สร้างตัวแปรสำหรับเก็บข้อมูล Title
all_product_url_raw = soup.find_all(class_ = "title")
all_product_url = []


#ทำการดึงข้อมูล URL ทั้งหมด และ ต่อ Path ให้ครบถ้วน
for i in all_product_url_raw :
    print("https://webscraper.io" + i.get("href"))
    all_product_url.append("https://webscraper.io" + i.get("href"))


#ลิสต์สำหรับเก็บข้อมูล Product ทั้งหมด
products = []


#ทำการวนซ้ำเพื่อดึงข้อมูลจากทุก URL
for i in all_product_url :
    
    #ระบุ Destination จาก URL ที่เก็บมา
    destination = requests.get(i)
    soup = BeautifulSoup(destination.content, 'html.parser')
    temp = soup.find_all(class_ = "caption")


    #ทำการวนซ้ำเพื่อดึงเฉพาะข้อมูลที่ต้องการเพิ่มลงไปในลิสต์หลัก (products)
    for j in temp :
        print(j.text)
        products.append(j.text)