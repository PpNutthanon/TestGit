#หาตัวหารตัวเลขลงตัว
print("Range of program is [1,5000]")
a,divide=[],[]
number=int(input("Enter the number you want to know the divisor :"))
for i in range(1,5001):
    a.append(i)
for i in range(len(a)):
        if number%a[i]==0:
            divide.append(a[i])
print("The all of divisor of",number,"is =>",divide)



    
