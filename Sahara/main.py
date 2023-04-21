
#look up table
import math
#1#
T = [200, 210, 220, 230, 240, 250, 260, 270, 280, 285, 290, 295, 298, 300, 305, 310, 315, 320, 325, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550]
#2#
H = [199.97, 209.97, 219.97]
#3#
Pr = [0.3363, 0.3987, 0.4690]
#4#
U = [142.56, 149.69, 156.82]
#5#
Vr = [1707.0, 1512.0, 1346.0]
#6#
S = [1.29559, 1.34444, 1.39105]

i = str(input("[1]T\n[2]H\n[3]Pr\n[4]U\n[5]Vr\n[6]S\npls select number of input variable (1-6) : "))

if i == "1" :
    i = T
elif i == "2" :
    i = H
elif i == "3" :
    i = Pr
elif i == "4" :
    i = U
elif i == "5" :
    i = Vr
elif i == "6" :
    i = S


input_value = float(input("input value = "))

j = str(input("pls select number of output variable (1-6) : "))
if j == "1" :
    j = T
elif j == "2" :
    j = H
elif j == "3" :
    j = Pr
elif j == "4" :
    j = U
elif j == "5" :
    j = Vr
elif j == "6" :
    j = S


for k in range(len(i)):
    if i[k] > input_value:
        {
            j := j[k-1]+((input_value-i[k-1])*((j[k]-j[k-1])/(i[k]-i[k-1]))),
            #j := ((j[k]-j[k-1]) * ((input_value) - (i[k-1]))) + ((j[k-1]) * (i[k]-i[k-1])),
            print("\n\n**** the output value is %.4f ******" %(j))
        }
        break
    if i[k] == input_value:
        {
            print("\n\n**** the output value is %.4f ******" % (j[k]))
        }
        break