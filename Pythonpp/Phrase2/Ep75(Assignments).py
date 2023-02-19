#Assignmnet Find Telephone Number
# input:ตำรวจ => output: 191
data={"191":"แจ้งเหตุด่วน","1668":"โรงำยาบาล","1447":"ดับเพลิง"}
def search(message):
    for key,value in data.items():
        if value==message:
            print("Tel  :",key)
        else:
            print("ไม่มีข้อมูล")
message=input("Enter Infomation You Want To Call :แ")
search(message)