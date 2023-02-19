#การเขียน Text Files
try:
    fw=open("pp.txt","w",encoding="utf-8")
    fw.write("Hello World\n")
    fw.writelines("Happy555")
    fw.close()
except FileNotFoundError:
    print("Cannot Find")