'''
Candela Kevarkian
Utilizar For
Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
mostrar el mayor.

'''
lista =[ 1, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58 ]

bandera = True
mayor = lista[0]

for i in lista:
    if i > mayor:
        mayor = i

print(f"El mayor numero es: {mayor}")