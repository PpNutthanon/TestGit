#Assignment Fibonacci
# 0 1 1 2 3 5 8 13 21 44
#f0 = ? , f1 = ?
def fibonacci(number):
    if number<=1:
        #เลขสองลำกับแรก
        return  number
    else:
        #เลขลำดับถัดไป
        return fibonacci(number-1)+fibonacci(number-2)
fib=int(input("Enter The Number of Fibonacci :"))
for i in range(fib+1):
    print(fibonacci(i))
