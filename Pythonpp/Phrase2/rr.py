def fibonacci(number):
    if number<=1:
        return number
    else:
        return fibonacci(number-1)+fibonacci(number-2)
fib=int(input("Enter Amount Series of Fibonacci :"))
for i in range(fib+1):
    print(fibonacci(i))