# Tuples , Sets , Dictionaries

#*Todo Tuple => Similair to lists but the diffrent is tuble can't be change or immutable
#* enclosed within ( )

a = ()
print(a)
print(type(a))

validlist = [1,2,"Hello",12.15,True,[3,4,5]]
validtuple = (1,2,3,"Hello",[3,4,5])
print(validlist)
print(validtuple)

print(validtuple[4])
print(validtuple[:2])
print(validtuple[3][0])

tuple1 = (1,2,3)
tuple2 = (2,3,4)
print("Before :",id(tuple1))
tuple1 = tuple1 + tuple2
print("After :",id(tuple1))


#*Todo Sets => Unorder , no duplicate , no index in this structure 
#* enclosed in {}
validset = {1,2,3}
print(type(validset),validset)
set1 = {1,2,3}
set2 = {2,3,1}
print(set1 == set2)

seta = set("abc")
print(seta)

#*Todo Mathematics Set Operations
set3 = {1,2,3}
set4 = {3,4,5}
print(set3 - set4)
print(set4 - set3)

#*Todo Symmetric Difference 
print(set3 ^ set4)

#*Todo Union symbol
print(set3 | set4)

#*Todo Intersection 
print(set3 & set4)


#*Todo Dictionaries => similiar to set unorderd , no duplicate but the different is Dictionaries need format of key:value
#The value can be anything (String , integer , float, Boolean) 
#! Left hand side can't be the same 
#* enclosed with { }
validdictionaries = {"Key1":22, "Key2":"Hello", "Key3":True}
print(validdictionaries)
scores = {
    "DataGuy":4,
    "Smuffy":1,
    "Moodre":7,
    "Mimi":3,
    "Ruji":1
}
print(scores)
scores["DataGuy"] = 5
scores["Ruji"] = scores["Ruji"] + 1
print(scores)
#** Dictionaries can searh by using the key

#*Todo .keys() & .values() 
print(scores.keys())
print(scores.values())
