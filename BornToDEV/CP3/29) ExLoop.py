number = int(input("Enter the number you want :"))
for i in range(number+1):
    print("*"*i)

text = ""
for i in range(number):
    text = text+"*"
    print(text)

for x in range(number):
    text = ""
    for y in range(x+1):
        text += "*"
    print(text)