#JUEGO DE ORDEN
import os
import time
import random

def Tutorial():             #TUTORIAL
    for i in range (5):
        os.system("cls")
        if i % 2==0:
            print("-_-_-_-_-_-_-_JUEGO DE ORDEN_-_-_-_-_-_-_-_-_-") 
            print("En el juego de orden tienes")
            print("que conseguir que todos los",end=" ")
            print("        1 2 3")
            print("los números en la mesa sean",end=" ")
            print("      A 1 1 1")
            print("1, indicando el punto según",end=" ")
            print("      B 1 1 1")
            print("la FILA y COLUMNA, como el",end=" ")
            print("       C 1 1 1")
            print("ejemplo de la derecha",end=" ")
            print("             -B2-")
        else:
            print("-_-_-_-_-_-_-_JUEGO DE ORDEN_-_-_-_-_-_-_-_-_-")
            print("En el juego de orden tienes")
            print("que conseguir que todos los",end=" ")
            print("        1 2 3")
            print("los números en la mesa sean",end=" ")
            print("      A 1 0 1" )
            print("1, indicando el punto según",end=" ")
            print("      B 0 0 0")
            print("la FILA y COLUMNA, como el",end=" ")
            print("       C 1 0 1")
            print("ejemplo de la derecha",end=" ")
            print("             -B2-")
        time.sleep(2)
    print("¿listo?")
    time.sleep(3)           # FIN TUTORIAL

def validar(rpta):          #VALIDACIÓN DE RPTA
    rpta = rpta.upper()
    if (rpta[0]=="A" or rpta[0]=="B" or rpta[0]=="C" or rpta[0]=="D" or rpta[0]=="E") :
        vera = True
    else:
        vera = False

    if vera:
        if rpta[1]=="1" or rpta[1]=="2" or rpta[1]=="3" or rpta[1]=="4" or rpta[1]=="5":
            vera = True
        else:
            vera = False

    return vera             #FIN DE VALIDACION RPTA

def PantallaInicio():       #PANTALLA DE INCIO
    os.system("cls")
    print ("-_-_-_-_-_-_-_JUEGO DE ORDEN_-_-_-_-_-_-_-_-_-")
    print ("Ingresa cualquier tecla")
    print ("para empezar.")
    print ("")
    print ("                        O ingresa X para ir al")
    print ("                                   al tutorial")
    ini = input()
    if ini == "x" or ini == "X":
        Tutorial()          # FIN DE PANTALLA DE INICIO

def GProblema(num):         #GENERADOR DE PROBLEMAS
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
    elif num==30:
        Cod="0011101111111111111111111"
        # Código para Debug
    else:
        print("No se ingresó generador de problema válido")
    return Cod              #FIN DE GENERADOR DE PROBLEMAS


PantallaInicio()

print(" -INICIANDO JUEGO-")
time.sleep(2)

#Se inician las variables priincipales
letras = "ABCDE"

#Se crea y diseña la lista del problema
ProblemaL = []
CodProblema = random.randint(1,5)                    # -> CAMBIAR ESTO PARA EL FINAL "random.randint(1,5)"
CodProblema = GProblema(CodProblema)

for x in CodProblema:
    ProblemaL.append(x)


while True:
    
    os.system("cls")
    #Impresora del Problema
    print ("     1  2  3  4  5")
    for x in range(5):
        print (letras[x], " - ", end ='')
        for y in range(5):
            print (ProblemaL[(x*5+y)], " ", end = '')
        print ("")
    

    #Se ingresa la rpta
    print (" > Ingresa tu RPTA, primero LETRA Y NUMERO ")
    rpta = str(input())
    
    #Se califica si es reset, entonces se regresa la lista a inicial
    if rpta=="reset" or rpta=="RESET":
        print ("R E I N I C I A N D O...")
        time.sleep(2)
        del ProblemaL[:]
        for x in CodProblema:
            ProblemaL.append(x)
        continue

    #Caerá en un bucle caso sea invalida el ingreso
    while True:    
        if validar(rpta):
            break
        else:
            time.sleep (1)
            print ("- Tu rpta es invalida -")
            print ("------------------------")
            print ("Debes ingresar LETRA y NÚMERO")
            rpta = str(input())

    #Se inicia el procesamiento de la respuesta ingresada
    print (" P R O C E S A N D O . . . ")
    time.sleep(1)

    cambio = []

    if rpta[0]=="A" or rpta[0]=="a":
        cambio.append("1")
    if rpta[0]=="B" or rpta[0]=="b":
        cambio.append("2")
    if rpta[0]=="C" or rpta[0]=="c":
        cambio.append("3")
    if rpta[0]=="D" or rpta[0]=="d":
        cambio.append("4")
    if rpta[0]=="E" or rpta[0]=="e":
        cambio.append("5")

    cambio.append(rpta[1])

    #Se define un "punto clave"
    k = (int(cambio[0])*5)-(5-int(cambio[1]))-1

    #Se define la lista _Cambio_ a partir del punto clave
    del cambio[:]
    cambio.append(int(k))
    if not (k%5==0):
        cambio.append(int(k-1))
    if (k not in (4, 9, 14, 19, 24)):
        cambio.append(int(k+1))
    cambio.append(int(k+5))
    cambio.append(int(k-5))

    #Ahora trabaja la lista cambio
    for n in cambio:
        if n>=0 and n<=24:
            if ProblemaL[n]=="1":
                ProblemaL[n]="0"
            else:
                ProblemaL[n]="1"

    #Se valida si el problema está completado
    ValP = 1
    for x in ProblemaL:
        ValP = ValP*int(x)
    if ValP==1:
        break


# Desde aquí, se terminó satisfactoriamente el juego
os.system("cls")
print ("-_-_-_-_-_-_ FELICIDADES _-_-_-_-_-_-")
print ("")
print ("     1  2  3  4  5")
for x in range(5):
    print (letras[x], " - ", end ='')
    for y in range(5):
        print (ProblemaL[(x*5+y)], " ", end = '')
    print ("")
print ("")
print (" _-_- GANASTE -_-_ ")
