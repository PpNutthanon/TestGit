#alculate number of days between two dates
from datetime import date
print("First date you want")
a=int(input("Enter the year(A.D) :"))
b=int(input("Enter month :"))
c=int(input("Enter the days :"))
print("\n")
print("Second date you want")
x=int(input("Enter the year(A.D) :"))
y=int(input("Enter month :"))
z=int(input("Enter the days :"))
print("\n")
first=date(a,b,c)
last=date(x,y,z)
diff= first - last
print("The difference between date is :",diff.days,"days")