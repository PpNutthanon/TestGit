
#Assignment for while loop(หาผลรวมตัวเลข)
number = int(input("Enter number you want :"))
sum = 0
i=1
#1+2+3+4+5
while i<=number:
    sum+=i #เก็บผลรวมของiแต่ละรอบ
    print("รอบที่",i,"ค่าsum เท่ากับ",sum)
    i=i+1
print("The sum of the number is :",sum)
print("The average value is",sum/number)
#Program Calculate Summation of Even Number
number = int(input("Enter the number :"))
i = 2
sum = 0
while i<=number:
    sum +=i
    i+=2
print(sum)
 