from bs4 import BeautifulSoup
import requests
import xlsxwriter
import pandas as pd
 


destination = requests.get("https://www.borntodev.com/online-course/")
soup = BeautifulSoup(destination.content, 'html.parser')


all_courses_raw = soup.find_all(class_ = "woocommerce-loop-product__title")
all_courses = []


for i in all_courses_raw :
    print(i.text)
    all_courses.append(i.text)


# สร้าง DataFrame ที่มี 1 คอลัมน์ชื่อ 'Data'
dataframe = pd.DataFrame({'Data' :  all_courses})
 
# สร้าง Pandas Excel Writer เพื่อใช้เขียนไฟล์ Excel โดยใช้ Engine เป็น xlsxwriter
# โดยตั้งชื่อไฟล์ว่า 'simple_data.xlsx'
writer = pd.ExcelWriter('simple_data.xlsx', engine='xlsxwriter')
 
# นำข้อมูลที่สร้างไว้ในตัวแปร dataframe เขียนลงไฟล์
dataframe.to_excel(writer, sheet_name='หน้าที่1')
 
# จบการทำงาน Pandas Excel writer และเซฟข้อมูลออกมาเป็นไฟล์ Excel
writer.save()