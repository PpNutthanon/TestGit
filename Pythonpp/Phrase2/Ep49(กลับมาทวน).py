#การค้นหาจำนวนตัวอักษรในสมาชิก
message=["aaa","aab","cba","cca","bba"]
result=[]
for item in message:
    item.count("a")
    result.append(item.count("a"))
print(result)