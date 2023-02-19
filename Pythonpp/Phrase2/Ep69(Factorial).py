#Assignment Factorial
number=int(input("Enter The Number of Factorial You Want :"))
def factorial(number):
    if number==1:
        return number
    else:
        return number*factorial(number-1)
answer=factorial(number)
print("The Answer of",number,"Factorial is :",answer)
'''
3!
3
3 x factorial(2)
3 x 2 x fatorial(1)
3 x 2 x 1 = 6
'''

