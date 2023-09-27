'''
Candela Kevarkian
Pedir el nombre y el sueldo, incrementarle un 10% e informar el 
aumento de su sueldo para esa persona.'''

nombre = input("Ingresa tu nombre")
sueldo = input("Ingresa tu sueldo ")
sueldo = int(sueldo)

porcentaje = sueldo * 10 / 100 
sueldo_incrementado = sueldo + porcentaje


print(f"El nuevo sueldo es de {sueldo_incrementado}")