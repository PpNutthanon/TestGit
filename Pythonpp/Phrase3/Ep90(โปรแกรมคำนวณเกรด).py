#Assignment โปรแกรมคำนวณเกรดของนักเรียน
#Input ป้อนรหัสนักเรียน พร้อมกับคะแนนที่สอบได้
'''
try:
    fw=open("score.txt","w",encoding="utf-8")
    print("Already Create File")
    while True:
        studentid=input("Enter The Student Id:")
        if studentid=="exit":
            break
        score=(input("Enter The Score of The Exam :"))
        fw.writelines(studentid+"\t"+score+"\n") #เขียน Studentid แล้วต่อด้วยคะแนน
    fw.close()
except Exception as problem:
    print("The Program Error Because :",problem)
'''
fr=open("score.txt","r",encoding="utf-8")
fw=open("grade.txt","w",encoding="utf-8")
grade=None
for line in fr.readlines():
    score=line[-4:].strip() #stripคือตัดช่องว่างทิ้งไป
    studentid=line[0:9].strip()
    score=int(score)
    if score>=80:
        grade="A"
    elif score>=70 and score<80:
        grade="B"
    elif score>=50 and score<70:
        grade="C"
    else:
        grade="F"
    
    print("Student ID :",studentid,"Score :",score,"Grade :",grade)
    fw.writelines(studentid+"\t"+str(score)+"\t"+grade+"\n")
fw.close()