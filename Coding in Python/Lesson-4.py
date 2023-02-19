# List and List Comprehension
variable = True
variable = 12
variable ="Hi"
print(variable)

#*todo List is comma seperated items enclosed with []
store = ["A","B","C"]
print(store)
print(store[0])
store[0] = "Pp" 
print(store)

#? Append & Insert
list1 = ["aa","bb","cc"]
list1.append("ee")
print(list1)
list1.insert(0,"Nutthanon") #*todo Add Nutthanon to index 0 of list1
print(list1)

#? Manipulate Lists
list2 = [1,2,3,4,5,6]
print(list2)
list2.pop()
print(list2)
list2.remove(2)
print(list2)
list2.clear()
print(list2)

# Spit the lists 
name = input("Team member name :")
name = name.split(",")
print(name)

#*todo Sort command
names = input("Active Member Name :")
names = names.split(",")
names = names.sort()
print(names)