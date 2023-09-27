'''
Candela Kevarkian

Pedir una edad. Informar si la persona es mayor de edad (más de 18 años),
adolescente (entre 13 y 17 años) o niño (menor a 13 años).'''

edad = input("Ingrese su edad")
edad = int(edad)

if edad <17:
    if edad > 13:
        print("Es adolescente")
    else:
        print("Es niño")

else:
    print("Es mayor de edad")




