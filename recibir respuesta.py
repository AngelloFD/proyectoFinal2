def es_letra_o_numero(comando):
    let = comando[0]
    num = comando[1]
    check = any(str.isdigit(let) for char in let)
    if check == False:
        check = any(str.isdigit(num) for char in num)
        if check == True:
            return True
        else:
            return False
    else:
        return False




a = input("Ingrese una letra y un numero: ")
print(a[0])
print(a[1])
print(es_letra_o_numero(a))