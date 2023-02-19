# MNIST Dataset => ใช้sklean กับ โหลดตัวเต็มเข้ามาทำงาน
from sklearn import datasets
digit_dataset = datasets.load_digits()
print(digit_dataset.keys())
print(digit_dataset["DESCR"]) #Description
print(digit_dataset["images"].shape)

print(digit_dataset["target_names"]) #ตัวเลข 0-9
print(digit_dataset.target_names) #*todo ผลลัพธ์เหมือนบรรทัดที่ 7

print(digit_dataset.images[1])
print(digit_dataset.images[1].shape) #เช็คขนาดรูปที่ 1

