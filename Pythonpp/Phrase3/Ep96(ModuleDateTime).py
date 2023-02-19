#module date and time => อยู่ใน module แบบ built in function
import datetime #Format จะเป็น ปี เดือน วัน เวลา
time=datetime.datetime.now() #ดึงวันเวลาปัจจุบันมาใช้งาน
print(time)
print(time.year) #แสดงเฉพาะปี
print(time.month) #แสดงเฉพาะเดือน

#แสดงวันที่ที่เรากำหนด
newdate=datetime.datetime(2020,6,20,15)
print(newdate)

#รูปแบบการแสดงผล
print(time)
print(time.strftime("%x")) #%x คือ เปลี่ยนรูปแบบวันที่เป็นแบบที่สั้นลง EX 05/26/21 จะแสดงเป็น เดือน/วัน/ปี
print(time.strftime("%X")) #%X ตัวใหญ่ จะแสดงเวลา แต่ %x ตัวเล็ก จะแสดง เดือน วัน ปี
print(time.strftime("%c")) #%c บอกเพิ่มมาว่า วันนี้เป็นวันอะไร

#เวลา
print(time.strftime("%H")) #แสดงเฉพาะเวลาที่เป็นชั่วโมง
print(time.strftime("%M")) #แสดงเฉพาะเวลาที่เป็นนาที
print(time.strftime("%H:%M:%S %p")) #%p ให้แสดงว่าตอนนี้เป็น AM หรือ PM

#หาผลต่างของวัน
print(time.strftime("%j")) #วันนี้ห่างจากปีใหม่มากี่วัน

#date
print(time.strftime("%a")) #%a คือการบอกวันอย่างเดียว(Mon Wed)
print(time.strftime("%A")) #%A บอกวันอย่างเดียวเหมือน %a แต่จะพิมชื่อเต็มของวันนั้น(Monday Wednesday)
print(time.strftime("%w")) # %w บอกว่าวันนี้เป็นวันที่เท่าไหร่ของสัปดาห์นี้
print(time.strftime("%d")) #%d แสดงเฉพาะวันที่
print(time.strftime("%b")) #%b แสดงเฉพาะเดือน แบบชื่อย่อเดือน
print(time.strftime("%B")) #%B แสดงเฉพาะเดือน แบบชื่อเต็มเดือน
print(time.strftime("Date %d Day %A Month %B Year %Y "))

#วันเดือน/เดือน/ปี
print(time.strftime("%d/%m/%Y"))