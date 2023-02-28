nickname = input("Enter your nickname: ")
weight = float(input("Enter your weight:"))
print("Hello "+nickname+" and weight is",weight,"kg")
print("Hello %s and weight is %d" % (nickname, weight)) 
# %s => String
# %d => Integer
# %f => Float