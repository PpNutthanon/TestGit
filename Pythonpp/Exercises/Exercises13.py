#Calculate the sum of three given numbers, if the values are equal then return thrice of their sum
sum=0
x=float(input("Enter the value :"))
y=float(input("Enter the value :"))
z=float(input("Enter the value :"))
if x==y==z:
     sum=(x+y+z)*x
else:
    sum=x+y+z
print("The sum is :",sum)

