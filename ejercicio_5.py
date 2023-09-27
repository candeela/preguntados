'''
Candela Kevarkian
Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000
por cada estadía como base, se pide el ingreso de una estación del
año(Invierno/Verano/Otoño/Primavera) y localidad (Bariloche/Cataratas/Mar del
Plata/Córdoba) para vacacionar para poder calcular el precio final:
-en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un
descuento del 10% Mar del Plata tiene un descuento del 20%
-en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene
un aumento del 10% Mar del Plata tiene un aumento del 20%
-en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un
aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el
precio sin descuento.
Validar el ingreso de datos
'''
estacion = input("Ingrese la estacion del año en la que desea viajar")
while estacion != "Invierno" and estacion != "Verano" and estacion !="Otoño" and estacion !="Primavera":
    estacion = input("Reingrese la estacion del año en la que desea viajar")

localidad = input ("Ingrese el destino de su viaje")
while localidad != "Bariloche" and localidad != "Cataratas" and localidad !="Mar del Plata" and  localidad != "Cordoba":
    localidad = input ("Ingrese el destino de su viaje")


base = 15000
base = int(base)

match estacion: 
    case "Invierno" :
        if localidad == "Bariloche":
            total = base + (base * 20 / 100) 


        elif localidad == "Mar del Plata":
            total =  base - (base * 20 / 100) 

        else:
            total =  base - (base * 10 / 100) 

    case "Verano":
        if localidad == "Bariloche":
            total =  base - (base * 20 / 100) 

        elif localidad == "Mar del Plata":
            total = base + (base * 20 / 100) 

        else:
            total = base + (base * 10 / 100) 

    case "Otoño"  | "Primavera":
        if localidad == "Cordoba":
            total = base
        else:
            total = base + (base * 10 / 100) 


print(f"El total del viaje es de {total} pesos")
