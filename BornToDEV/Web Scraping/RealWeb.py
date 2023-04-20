from bs4 import BeautifulSoup
import requests

#Todo: ดึงข้อมูล Website ก่อน
destination = requests.get("https://www.midjourney.com/app/feed/?sort=rising")
soup = BeautifulSoup(destination.content, "html.parser") #Todo: แปลงเป็นไฟล์ HTML
print(soup.title)
print(soup.img)

#Todo: หาชื่อ class ที่ชื่อ prices
print(soup.find_all(class_ = "prices"))