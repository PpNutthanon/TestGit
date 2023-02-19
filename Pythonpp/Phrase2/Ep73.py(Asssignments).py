'''
#Assignment Function Addition
def add(*number):
    sum=0
    for i in range (len(number)):
        sum+=number[i]
    print("The Value Of Addition All Number Is :",sum)
add(2,3,4,5,6,7,8,9,10)
'''
#Assignment Function Addition Type2 (The Best)
def summation(number):
    total,average=0,0
    for i in number:
        total+=i
    average=total/len(number)
    return total,average
x=[1,2,3,4,5]
y,z=summation(x)
print(y)
print(z)
'''
#Assignment Function Average
def average(*num):
    a=0
    for i in range (len(num)):
        a+=num[i]
    avr=a/len(num)
    print("The Average Value Of All Number Is :",avr)
average(2,3,4,5,6,7,8,9,10)
'''