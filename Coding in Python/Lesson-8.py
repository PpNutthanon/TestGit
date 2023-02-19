# Errors and Exceptions

#*? 3 Base Types of Error
#      1) Syntax Error => Happen when Python doesn't understand our code such as print("NFT)
#*Todo 2) Runtime Error => Python understands our code but runs intotrouble when running our code such as zerodivisionError
#**    3) Logic Error => Python understands our code, no trouble running our code but doesn't archeive what you want to do

# try catch 
try:
    number = int(input("Number of people involved :"))
    share = (1/number)  *100
    print("Each person will get share of :",share,"%")
except:
    print("Bro! Invalid Numbers")