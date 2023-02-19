# More about Dictionaries
#*Todo Keys can be anything that immutable
scores = {
    "Key":100,
    "Pp":200,
    (1,2,3):300
}
print(scores,scores["Pp"])
print(scores[(1,2,3)])
print(len(scores)) # Count the number of keys we have in Dictionary
scores["Pp"] = 500
print(scores)


dict()
newDict = dict(a=1, b=2, c=3)
print(newDict,dict())
#! We can't pop in dictionary because no index in Dictionaries


scorelist = [1,2,3]
scorelist.pop()
print(scorelist)

print("Pp" in scores)
print("Pp" not in scores)

complex = {
    1:[0,1,["aa","bb"],(1,2)],
    10230:(1,(0,1))
}
print(complex.keys())
print(complex.values())
print(complex.items()) #Lists of key values in Dictionaries

#for key.value in scores.items():
 #  print(key,"=")  

answer = input("Answer :")
tally = {}
while answer != "" :
    if answer not in tally:
        tally[answer] = 1
    else:
        tally[answer] += 1
    answer = input("Answer :")
print(tally)
#Key cannot contain duplicates
