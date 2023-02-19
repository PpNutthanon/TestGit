#ลำดับความสำคัญของตัวดำเนินการทางคณิตศาสตร์
'''
1) Parentheses(วงเล็บ)
2) -,+,--,++,sizeof,(type) (Unary operators)เป็นการเพิ่มและลดค่า (Right to left)
3) *,/,% (ทำงานจากซ้ายไปขวา)
4)+,- (ทำงานจากซ้ายไปขวา)
5)=
'''
x = 5+2*10
print("The value of x is :",x)
x = (5+2)*10
print("The value of x is :",x)
x = (5+2)*10/2
print("The value of x is :",x)
x = (5+2)/10*2 
print("The value of x is :",x)
x = (5+2)/(10*2)
print("The value of x is :",x)
x = 5+2/10*2-5
print("The value of x is :",x)



