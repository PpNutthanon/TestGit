#Program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers
a=[]
for i in range(4):
    b = int(input("Enter the number :"))
    a.append(b)
print("Sample data:",a[0],",",a[1],",",a[2],",",a[3])
print("Output :")
print("List :",a)
print("Tuple :",tuple(a))