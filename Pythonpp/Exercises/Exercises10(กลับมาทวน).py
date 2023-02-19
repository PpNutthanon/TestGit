#Program to print the calendar of a given month and year
import calendar
year = int(input("Enter year you want(A.D.) :"))
month = int(input("Enter monrth you want :"))
print(calendar.month(year,month))
