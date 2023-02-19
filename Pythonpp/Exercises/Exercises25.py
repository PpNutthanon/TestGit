#Assignment Find Sum Of All Number By Function
def add(x):
    sum=0
    for i in range(len(x)):
        sum+=x[i]
    print("The Summation of All Number is :",sum)
x=[]
amount=int(input("Enter Amount Of Number You Want to Add :"))
for i in range(amount):
    number=float(input("Enter The number :")) 
    x.append(number)
print("All Of Number You Input Are :",x)
add(x)

    