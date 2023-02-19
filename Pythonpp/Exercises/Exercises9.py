#Program accepts integer computes value n+nn+nnn
number = int(input("Enter the value you want :"))
a= str(number)+str(number)
b = str(number)+str(number)+str(number)
a,b=int(a),int(b)
value = number+a+b
print("The value is :",value)

    
    