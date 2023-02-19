# Conditionals & String Manipulations
name = input("What is your name :")
if name == "cmtat":
    print("Your majestry")
else:
    print("Good Moring")

if name != "cmtat":
    print("Your majestry")
else:
    print("Good Moring")

#*Todo Boolean Data Type => True or False
print("aa"=="aa")

age = int(input("How old are you :"))
if age < 18 and age > 16:
    print("You are underage")
elif age < 21:
    print("Hmm")
else:
    print("You are old")

# Indexing
names = "Nutthanon"
print(names[0])
print(names[0:3])
print(names[0:])
print(names.replace("N","P"))
print(names.upper())
print(names.lower())

search = "macbookpro"
product = "Macbook Pro"
if search in product.lower().replace(" ",""):
    print("Found it")
elif  search not in product.lower():
    print("Product not found")

password = "123456"
if(len(password)<6):
    print("Password is too short")
else:
    print("Strong enough")
