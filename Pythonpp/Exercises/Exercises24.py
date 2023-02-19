#Assignment Use Function To Find Maximum Number Of 3 Number
def max(a,b,c):
    if a>b:
        num(a,c)
    elif b>a or a==b:
        num(b,c)
    
def num(A,B):
    if A>B:
        print(A,"is maximum number")
    if B>A or B==A:
        print(B,"is maximum number")  