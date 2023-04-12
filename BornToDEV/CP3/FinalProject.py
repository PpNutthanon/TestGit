# Import necessary libraries 
import os #Todo: ค้นหา, จัดการ, อ่าน, เขียน, ลบ ไฟล์ต่างๆภายในเครื่อง
import shutil #Todo: provides a convenient way to manipulate files and directories เช่น copy, เคลื่อนย้ายไฟล์, จัดการไฟล์
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

# Todo: Create Dictionary that lists various of file Types
file_categories = {
    ".txt": "Text",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".pdf": "Documents",
}


def organize_files(path): #Todo: Create function that input the path which path is the location of the folder we want to organize files
    for file in os.listdir(path): #Todo: ให้ file เป็น lists ของ Folder,files ทั้งหมดที่อยู่ใน path
        file_path = os.path.join(path, file) #Todo: เชื่อมต่อ path ของโฟลเดอร์กับชื่อของไฟล์หรือโฟลเดอร์เราต้องการจัดการเข้าด้วยกัน

        if os.path.isfile(file_path): #Todo Check ว่าภายใน file_path มีอะไรที่ไม่เป็น folder มั้ย เช่น .png .pdf .py ...etc...
            file_extension = os.path.splitext(file)[1].lower() #Todo: เช็คว่าแต่ละไฟล์ นามสกุลอะไรบ้าง
            if file_extension in file_categories: #Todo ตรวจสอบว่าไฟล์ที่เราใส่เข้าไปเป็นไฟล์ประเภทไหน
                category = file_categories[file_extension] #Todo ให้แสดงว่าเป็นไฟล์ประเภทไหนที่อยู่ใน file_categories ex. image, text, documents
                category_folder = os.path.join(path, category) #Todo: เชื่อมต่อ path ของโฟลเดอร์กับชื่อของไฟล์หรือโฟลเดอร์เราต้องการจัดการเข้าด้วยกัน

                if not os.path.exists(category_folder):
                    os.makedirs(category_folder) #Todo: สร้างโฟลเดอร์ ในระบบไฟล์ของเครื่องคอมพิวเตอร์

                destination = os.path.join(category_folder, file)
                shutil.move(file_path, destination) #Todo ย้ายไฟล์ไปโฟลเดอร์ที่เราต้องการจัดเก็บ

def browse_directory():
    directory_to_organize = filedialog.askdirectory() #Todo จาก tkinter function => เปิดกล่องโต้ตอบ (dialog box) ขึ้นมา เพื่อให้ผู้ใช้เลือกโฟลเดอร์ที่ต้องการจัดการไฟล์ เมื่อผู้ใช้เลือกโฟลเดอร์แล้ว โปรแกรมจะเก็บที่อยู่ของโฟลเดอร์ที่ผู้ใช้เลือกไว้ในตัวแปร directory_to_organize
    organize_files(directory_to_organize) #Todo เรียกใช้งาน function organize_files
    result_label.config(text="Files have been organized!.") #Todo โชว์ว่าไฟล์ทำการจัดเก็บเรียบร้อยแล้ว

def start_organization():
    root.update()
    browse_directory()

root = tk.Tk()
root.title("File Organizer") #Todo: แสดงคำพูดที่แท็บข้างบน
root.geometry("350x150") #Todo กำหนดขนาดความกว้าง ความยาว ของหน้าต่างโปรแกรม หลังจากกด run
root.config(bg="#1DB954") #? White color เลือกสีของ background ใน tkinter 

title_label = tk.Label(root, text="File Organizer", font=("Arial", 18),fg="#1DB954", bg="#191414")
title_label.pack(pady=20) #Todo: ปรับแกนyลงมา 10 จากขอบข้างบน

browse_button = tk.Button(root, text="Select Directory", command=start_organization,fg="#1DB954", bg="#191414", font=("Arial", 12))
browse_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12),fg="#1DB954", bg="#191414") #Todo: หลังจากเสร็จจะเปลี่ยนเป็น "Files have been organized" เหมือนใน code บรรทัดที่ 37
result_label.pack(pady=10)

root.mainloop()