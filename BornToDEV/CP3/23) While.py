# While Loop => ทำงานไปเรื่อยๆ จนกว่าเงื่อนไขจะกลายเป็นเท็จ
while False:
    print("Hello")
correct = 67
number = 0
while number != correct:
    number = int(input("Please guess the number :"))
    if correct == number:
        print("Congratulations")
    elif number > correct:
        print("Too high")
    elif number < correct:
        print("Too low")