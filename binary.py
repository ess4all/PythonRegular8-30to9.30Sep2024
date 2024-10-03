x = 30
bi = ""
d = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
while x>=1:
    rem = x%16
    if rem>=0 and rem<=9:
        bi=str(rem)+bi
    else:
        bi = d[rem]+bi

    print("==> ",rem)

    x=x//16

print(bi)


