'''
Candela Kevarkian

Dadas las siguientes listas:
edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]
y considerando que la posición en la lista corresponde a la misma persona,
mostar el nombre de la persona más joven


'''
lista_edades = [25 ,36 ,18 ,23 ,45]
lista_nombres = [ "Juan","Ana","Sol","Mario","Sonia"]


joven = lista_edades[0]


for i in lista_edades:
    if i < joven:
        joven = i
print(f"La persona mas joven tiene: {joven} años")

for i in range(len(lista_edades)):
    edad = lista_edades[i]
    nombre = lista_nombres[i]

    if joven == edad:
        print(f"el nombre de la persona mas joven es:{nombre} ")
