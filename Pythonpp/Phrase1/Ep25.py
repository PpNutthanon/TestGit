
#โปรแกรมแปลง celicus => farenheit or farenheit => celcius
temp = input("Enter temperature and unit of temperatue : ")
degree = float(temp[:-1]) #เอาทุกตัวยกเว้นตัวสุดท้าย
unit = temp[-1].upper() #เอาแค่ตัวสุดท้าย
print(degree,unit)
print(type(degree))
if "C" in unit:
    Farenheit = ((degree*9)/5) +32
    print("Your Temperature in Farenheit is :",Farenheit)

elif "F" in unit:
    Celcius = ((degree -32)*5)/9
    print("Your Temperature in Celcius is :",Celcius)
#Program Calculate Kelvin => Celcius & Celcius => Kelvin
print("1) Kelvin  => Celcius")
print("2) Celcius => Kelvin")
equation = int(input("Enter equation you want:"))
if equation==1:
    k = float(input("Enter your temperature in kelvin :"))
    c = k-273
    print("Your temperature in celcius is :",c)
elif equation==2:
    c = float(input("Enter your temperature is celcius:"))
    K =273+c
    print("Your temperature in kelvin is :",K)
else:
    print("Sorry the program is error")