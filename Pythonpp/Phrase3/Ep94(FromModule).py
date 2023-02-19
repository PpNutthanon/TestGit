#From Module => เข้าถึงเฉพาะ Function ที่เราต้องการจะเรียกใช้เท่านั้น
from CalculateServices import addition #import เฉพาะ Function addition
from CalculateServices import* #import ทั้งหมดแบบไม่ต้องพิม CalculateServices. 
from Weather import* #จะเรียกใช้งานแบบไม่ต้องพิม Weather.ได้เลย
addition(1,2) #ไม่ต้องมี CalculateServices นำหน้าแล้ว
print(PI)
print(city)

