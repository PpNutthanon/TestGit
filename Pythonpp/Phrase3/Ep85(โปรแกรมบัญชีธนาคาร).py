#Assignment โปรแกรมบัญชีธนาคาร
account={"PP":5000,"TT":100}
def getbalance(): #เช็คยอดเงินคงเหลือ
    print("Net Cost In Account :",account)
def deposit(money):
    if not type(money) is float:
        raise Exception("Must Be Enter The Number")
    if money<=0:
        raise Exception("Money You Deposit Must Be More Than Zero")
    print("Deposit money To Accont :",money)
    account["PP"]+=money
    getbalance()
def withdraw(money):
    if not type(money) is int:
        raise Exception("Must Be Enter The Number")
    if money<=0:
        raise Exception("Money You Withdraw Must Be More Than Zero")
    if money>account["PP"]:
        raise Exception("Your Money Doesn't Enough To Transfer")

    print("Withdraw Money Out Of Account :",money)
    account["PP"]-=money
    getbalance()
def transfer(money):
    if not type(money) is float:
        raise Exception("Must Be Enter The Number")
    if money<=0:
        raise Exception("Money You Transfer Must Be More Than Zero")
    if money>account["PP"]:
        raise Exception("Your Money Doesn't Enough To Transfer")
    print("Transfer Money A Account To B Account :",money)
    account["PP"]-=money
    account["TT"]+=money
    getbalance()
#มีErrorคือ 1)ฝากเงินเป็นค่าติดลบ 2)inputไม่ใช่ตัวเลข 3)ถอนเงินเกินยอดในบัญชี
try:
    getbalance()
    transfer(100)
except Exception as problem:
    print(problem)