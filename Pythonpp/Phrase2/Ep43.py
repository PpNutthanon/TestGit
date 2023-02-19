#Assignment หากลุ่มเลขคู่ฝเลขคี่
number=[]
even=[]
odd=[]
a = int(input("Enter the number of round:"))
for i in range(a):
    x = float(input("Emter the number :"))
    number.append(x)
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
number.sort()
even.sort()
odd.sort()
print("The number you input is:",number)
print("Even number is :",even)
print("Odd number is :",odd)
