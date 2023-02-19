# Assignment จับคู่คำทักทาย / บุคคล
'''
Hi,Hello
kong,gam
Hi kong,Ho gam,Hello kong,Hello gam
'''
greet = ["Sawasdee","Hi","Hello","GoodBye"]
person = ["kong","gam","joe"]
result=[]
#แบบปกติ
for i in greet:
    for j in person:
        result.append(i+j)
print(result)
#เขียนแบบลดรูป
answer = [x+y for x in greet for y in person]
print(answer)

a = ["Timming","Gam","Pinpak"]
b = ["Hi","Hello","ByeBye"]
result=[]
for i in b:
    for j in a:
        result.append(a+b)
print(result)


