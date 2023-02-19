#Assignment Find Amount of Big/Small Alphabet
#ABCdeF => พิมพ์ใหญ่ 4,พิมพ์เล็ก 2
def check(message):
    result={"UPPER":0,"LOWER":0}
    for c in message:
        if c.isupper():
            result["UPPER"]+=1
        elif c.islower():
            result["LOWER"]+=1
    return result 
message=input("Input Your Message :")
x=check(message)
print(x)
