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
        file_path = os.path.join(path, file) 

        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1].lower()

            if file_extension in file_categories:
                category = file_categories[file_extension]
                category_folder = os.path.join(path, category)

                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)

                destination = os.path.join(category_folder, file)
                shutil.move(file_path, destination)

def browse_directory():
    directory_to_organize = filedialog.askdirectory()
    organize_files(directory_to_organize)
    result_label.config(text="Files have been organized.")

def start_organization():
    root.update()
    browse_directory()

root = tk.Tk()
root.title("File Organizer")
root.geometry("350x150")
root.config(bg="#F0F0F0")

title_label = tk.Label(root, text="File Organizer", font=("Arial", 18), bg="#F0F0F0")
title_label.pack(pady=10)

browse_button = tk.Button(root, text="Select Directory", command=start_organization, bg="#A0A0A0", font=("Arial", 12))
browse_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#F0F0F0")
result_label.pack(pady=10)

root.mainloop()
