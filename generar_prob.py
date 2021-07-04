import random

def GProblema(num):
    while num>0:
        if num==1:
            CodPrm="0011001110110001011000010"
            # a1 + c4 + e2 + d5 + b5
        elif num==2:
            CodPrm="1100011010000001110100011"
            # e2 + c4 + c2 + b3 + a5
        elif num==3:
            CodPrm="0100000000001101100111011"
            # a1 + a3 + d3 + c2 + b5
        elif num==4:
            CodPrm="0000100111000010101000100"
            # c3 + a3 + e5 + b1 + e1
        elif num==5:
            CodPrm="1100010101001110100000000"
            # d3 + a4 + e5 + c2 + e1
        else:
            print("No se ingresó generador de problema válido")
    return num

CodPrm=0
print (CodPrm)
CodPrm = GProblema(random(1,5))

