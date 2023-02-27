def VAT(totalprice):
    result = totalprice*1.07
    return result
totalprice = float(input("Enter Price :"))
print("Price include VAT :",VAT(totalprice))
    