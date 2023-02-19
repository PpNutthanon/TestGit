#Program สูตรคูณ(เขียนเอง)
'''
number = int(input("Enter the number multiplication table you want :"))
i = 1
print("The Multiplication Table of",number)
for i in range(1,13):
    print(number ,"*",i, "=",number*i)
    i+=i
number =int(input("Enter the number multiplication you want :"))
i=1
print("The Multiplication Table of",number)
while i<=12:
    print(number,"*",i,"=",number*i)
    i+=1

#Program สูตรคูณ แบบในคลิป
start = int(input("Enter the number Multiplication Table you want start :"))
final = int(input("Enter the number Multiplication Table you ant to stop :"))
for x in range(start,final+1): #บวก1ให้สิ้นสุดที่สูตรคูณแม่ที่เรากรอกในfinal
    print("Multiplication Table :",x)
    for y in range(1,13):
        print(x,"*",y,"=",x*y)

'''




a=int(input("Enter the first multiplication table you want :"))
b=int(input("Enter the last multiplication table tou want:"))
for i in range(a,b+1):
    print("Multiplication Table:",i)
    for j in range(1,13):
        print(i,"*",j,"=",i*j)



