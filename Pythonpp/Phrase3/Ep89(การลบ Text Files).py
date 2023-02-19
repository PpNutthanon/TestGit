#ลบ Text Files
'''
try:
    fw=open("score.text","a",encoding="utf-8")
    for i in range(2):
        name=input("Enter The Message You Want :")
        fw.writelines(name+"\n")
    fw.close()
except FileNotFoundError:
    print("Cannot See The FIles")
'''
import os
try:
    if os .path.exists("Student.txt"):
        os.remove("Student.txt")
    else:
        print("Cannot See The Files")

except Exception as problem:
    print("The Problem Is :",problem)