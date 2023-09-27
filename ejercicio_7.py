'''
Candela Kevarkian
Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
mostrar solo los números pares.
'''
lista = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
lista_pares = [ ]

for i in lista:
    if i % 2 == 0:
        lista_pares.append(i)

print(lista_pares)
