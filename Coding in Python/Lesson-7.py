# Functions => reasurable block of code , usually performs a single task
def wave():
    print("Wave!")
    print("Hello IONS")
# Call & Execute The Function
for i in range(3):
    wave()

def wavesomeone(name):
    print("Hi "+ name)
    return name + " Hola"
newname = wavesomeone("Deeo")
wavesomeone("Nutthanon")
print(newname)

#* Functions can have multiple arguements
def totalprofit(sale1,sale2):
    total = sale1 + sale2
    return total
profit = totalprofit(1.2,0.8)
print("Total Profit is :",profit)


def totalFinal(*args):
    total = 0
    for sale in args:
        total += sale
    return total
print(totalFinal(1,2.3,5,6.8))

