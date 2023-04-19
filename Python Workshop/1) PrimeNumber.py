# Import math for calculation
import math
#Todo: Declare Variables use in Program
check_list, list_number, prime_number = [], [], []

#Todo: Input Value into Program
start = int(input("Enter the start number: "))
final = int(input("Enter the final number: "))
number = int(math.sqrt(final))

#Todo: Running the Condition
for i in range(3,number+1,2):
    check_list.append(i)
for i in range (start,final+1):
    list_number.append(i)
for i in list_number:
   
    if i !=2 and i % 2 ==0:
        list_number.remove(i)
    if i == 1 or i == -1:
        list_number.remove(i)


  
print("found:",len(prime_number))
print(prime_number)