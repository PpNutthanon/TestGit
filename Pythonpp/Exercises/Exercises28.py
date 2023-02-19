# Assignment อ่านตัวเลข3หลักเป็นคำอ่าน => 321 is Three Hundred And Twenty One
#*Todo Annouce The Function Of The Program And Input The Data To Calculate
print("Program Translate Number To Alphabet")
number = int(input("Please Enter The Integer Number (3 digits) :"))
number = str(number)

#*Todo Create Function To Change Number To Spelling 
def CheckSpelling(hundred,ten,digits):
    #! Check The Hundred Number
    if hundred=="0":
        messagehundred = ""
    elif hundred=="1":
        messagehundred = "One Hundred "
    elif hundred=="2":
        messagehundred = "Two Hundred "
    elif hundred=="3":
        messagehundred = "Three Hundred "
    elif hundred=="4":
        messagehundred = "Four Hundred "
    elif hundred=="5":
        messagehundred = "Five Hundred "
    elif hundred=="6":
        messagehundred = "Six Hundred "
    elif hundred=="7":
        messagehundred = "Seven Hundred "
    elif hundred=="8":
        messagehundred = "Eight Hundred "
    elif hundred=="9":
        messagehundred = "Nine Hundred "

    #! Check The Ten Number 
    if ten=="0":
        messagehundred = ""
    elif ten=="1":
        if digits=="0":
            messageten = "Ten"
        elif digits=="1":
            messageten = "Eleven"
        elif digits=="2":
            messageten = "Twelve"
        elif digits=="3":
            messageten = "Thirteen"
        elif digits=="4":
            messageten = "Fourteen"
        elif digits=="5":
            messageten = "Fifteen"
        elif digits=="6":
            messageten = "Sixteen"
        elif digits=="7":
            messageten = "Seventeen"
        elif digits=="8":
            messageten = "Eightteen"
        elif digits=="9":
            messageten = "Nineteen"
            
    elif ten=="2":
        messageten = "Twenty"
    elif ten=="3":
        messageten = "Thirty"
    elif ten=="4":
        messageten = "Forty"
    elif ten=="5":
        messageten = "Fifty"
    elif ten=="6":
        messageten = "Sixty"
    elif ten=="7":
        messageten = "Seventy"
    elif ten=="8":
        messageten = "Eighty"
    elif ten=="9":
        messageten = "Ninty"

    #!Check The Main Digits
    if digits=="0":
        messagedigits = ""
    elif ten=="1":
        messagedigits = ""
    elif digits=="1":
        messagedigits = "One"
    elif digits=="2":
        messagedigits = "Two"
    elif digits=="3":
        messagedigits = "Three"
    elif digits=="4":
        messagedigits = "Four"
    elif digits=="5":
        messagedigits = "Five"
    elif digits=="6":
        messagedigits = "Six"
    elif digits=="7":
        messagedigits = "Seven"
    elif digits=="8":
        messagedigits = "Eight"
    elif digits=="9":
        messagedigits = "Nine"
    print(messagehundred+ "And " + messageten + "-" + messagedigits)

#*Todo Test The Results
CheckSpelling(number[-3],number[-2],number[-1])


  
