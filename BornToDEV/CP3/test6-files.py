from tkinter import filedialog
import os
import tkinter as tk
import shutil
from tkinter import ttk
dir_path = 'Pythonpp'
# get a list of all the files and directories in the specified path
dir_contents = os.listdir(dir_path)
# print the contents of the directory
print(dir_contents)
file_categories = {
     ".txt" : "text",
     ".png" : "image",
     ".jpg" : "image",
     ".pdf" : "documents",
     ".py"  : "python",
}
'''
for file in os.listdir(dir_path): 
        file_path = os.path.join(dir_path, file) 

        if os.path.isfile(file_path): 
            file_extension = os.path.splitext(file)[1].lower()
            print("Hello")
            print(file_extension)

            if file_extension in file_categories: #Todo ตรวจสอบว่าไฟล์ที่เราใส่เข้าไปเป็นไฟล์ประเภทไหน
                category = file_categories[file_extension] #Todo ให้แสดงว่าเป็นไฟล์ประเภทไหนที่อยู่ใน file_categories ex. image, text, documents
                category_folder = os.path.join(dir_path, category) 
                print(category)
                print(category_folder)

                if not os.path.exists(category_folder):
                    a = os.makedirs(category_folder)
                    print(a)
                print("\n")
'''

#directory_to_organize = filedialog.askdirectory()
#print(directory_to_organize)

def start_organization():
    root.update()

root = tk.Tk()
root.title("File Organizer") #Todo: แสดงคำพูดที่แท็บข้างบน
root.geometry("1050x150") 
root.config(bg="#1DB954")

title_label = tk.Label(root, text="Files Organizer Program", font=("Helvetica", 18),fg="#1DB954", bg="#191414")
title_label.pack(pady=20)

browse_button = tk.Button(root, text="Select Folder", command=start_organization,fg="#1DB954", bg="#191414", font=("Arial", 12))
browse_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12),fg="#1DB954", bg="#191414")
result_label.pack(pady=10)

root.mainloop()    