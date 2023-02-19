#อ่าน Text Files
#โครงสร้าง:open("ชื่อไฟล์","โหมด","การเข้ารหัส")
#r=read,w=write,a=append,x=create,t=textfile
try:
    fr=open("Student.txt","r")
    print(fr.read())
except FileNotFoundError:
    print("Cannot Find Text Files")