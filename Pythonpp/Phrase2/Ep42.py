#Assignment หาค่าสูงสุดต่ำสุดและผลรวมตัวเลข
number=[]
round = int(input("Enter how many number you want to add:"))
i=1
while i<=round:
    x = float(input("Enter the the number:"))
    number.append(x)
    i+=1
number.sort()
print(number)
print("The maximum value is :",number[-1])
print("The minimum value is :",number[0])
print(min(number))
print(max(number))
print(sum(number)) #หาผลรวมของlist