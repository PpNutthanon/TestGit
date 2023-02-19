#break/continue
i = 1
#break => หยุด
while i<=10:
    print("Round :",i)
    if i==5:
        break
    i+=1
#continue => กระโดดข้าม
j=1
while j<=10:
    j+=1
    if j%2 == 0:
        continue #ถ้ากระโดดข้าม บรรทัดที่15จะไม่ทำงาน
    print("Round :",j)
for k in range(1,11):
    if k%2==0:
        continue
    print(k)

print("Thank you for using program")