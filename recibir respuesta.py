#Validar letra and número
while True:

    print ("Digitar letra y numero")
Digitar = str(input())
print('First 5 caracthers: ', Digitar)
 

if (Digitar):
    print('Ha digitado un movimiento valido. ')

else:
    print('El valor digitado no corresponde con un movimiento valido. ')