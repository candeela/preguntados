'''
Candela Kevarkian

Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
mostrar el número repetido'''

lista = [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58, 29]
lista_repes = [ ]

for i in lista:
    if lista.count(i) > 1:
        lista_repes.append(i)
    
lista_repes = set(lista_repes)

print(lista_repes)