#Arbitary Arguments => argument หลายๆตัว(*agrs)
#เปลี่ยน agrs ไปเป็นอย่างอื่นได้หมดเลย

def add(*agrs):
    print("Your all inputs => ",agrs) #จะได้เป็น tuple
    sum=0
    for item in agrs:
        sum+=item
    print("The value of summation you input is =>",sum)
print(type(add))
add(10,20,40)
add(10,100) 



