#*todo 2 Major types of Loop => For Loop & While Loop
name = input("What is your name :")
while name != "" :
    name = input("What is your name :")
    print("Name Register :",name)

i=0
for j in range(3): # 0,1,2
    i=i+1
#* Execute the code 
print(i)

DiscordNames = ""
name = input("Participate in rumble, enter discord usernames : ")
while name != "":
    DiscordNames = DiscordNames + name + " "
    name = input("Participate in rumble, enter discord usernames :")
print(DiscordNames) 


