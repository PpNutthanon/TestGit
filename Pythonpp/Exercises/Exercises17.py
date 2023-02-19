#Program Check The Number Less Than 10
a=[2,3,5,8,13,21,34,55,89]
number=[]
print(len(a))
print(type(a))

for i in range(len(a)):
    if a[i]<=10:
        number.append(a[i])
print("The number less than ten is =>",number)