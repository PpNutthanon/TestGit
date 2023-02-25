Username = "0"
Password = "0"
while Username != "admin" or Password != "123" :
    Username = input("Username :")
    Password = input("Password :")
    if Username != "admin" or Password != "123":
        print("Incorrect username or password")
    elif Username == "admin" and Password == "123":
        print("You can login")