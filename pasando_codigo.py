letras = "ABCDE"
Problem[5,5]

print()
print("    ListaM  ")
print("  1 2 3 4 5")
for x in range(1,5):
    print(letras[x,x], end="")
    for i in range(1,5):
        print(Problem[x,i], end="")
    print()
