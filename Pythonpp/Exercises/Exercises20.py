#Mathematics Operation
a=int(input("Enter the number :"))
b=int(input("Enter the number :"))
if a*b>1000:
    print("The result is :",a+b)
else:
    print("The result is :",a*b)

#Sum of range
r=int(input("Enter the range :"))
sum=1
print("Current number 0"+" Previous Number 0","Sum : 0")
for i in range(1,r):
    print("Current number",i,"Previous Number",i-1,"Sum :",sum)
    sum+=2

#Seperate String
name=input("Enter the word :")
print(len(name))
for i in range(len(name)):
    if i%2==0:
        print(name[i])

#Remove String
word=input("Enter the word :")
num=int(input("Enter the number:"))
print(word[num:])

#Lists of the number
a=[10,20,30,30,40,10]
b=[10,20,30,40,50]
print("Given list is",a)
if a[0]==a[-1]:
    print("result is True")
else:
    print("result is False")
print("Given list is",b)
if b[0]==b[-1]:
    print("result is True")
else:
    print("result is False")

