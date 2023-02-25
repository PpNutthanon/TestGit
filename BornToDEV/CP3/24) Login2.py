Username = "0"
Password = "0"
while Username != "admin" or Password != "123" :
    Username = input("Username :")
    Password = input("Password :")
    if Username != "admin" or Password != "123":
        print("Incorrect username or password")
   
print("You can login")