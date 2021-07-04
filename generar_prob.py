import random

def GProblema(num):
    if num==1:
        Cod="0011001110110001011000010"
        # a1 + c4 + e2 + d5 + b5
    elif num==2:
        Cod="1100011010000001110100011"
        # e2 + c4 + c2 + b3 + a5
    elif num==3:
        Cod="0100000000001101100111011"
        # a1 + a3 + d3 + c2 + b5
    elif num==4:
        Cod="0000100111000010101000100"
        # c3 + a3 + e5 + b1 + e1
    elif num==5:
        Cod="1100010101001110100000000"
        # d3 + a4 + e5 + c2 + e1
    else:
        print("No se ingresó generador de problema válido")
    return Cod

codPrm = random.randint(1,5)
print (codPrm)
codPrm = GProblema(codPrm)
print (codPrm)


