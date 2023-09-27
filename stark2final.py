from data_stark import lista_personajes
from funciones_stark2 import *

while True:
    print('''a- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
b- Determinar cuál es el superhéroe más alto de género F
c- Determinar cuál es el superhéroe más alto de género M
d- Determinar cuál es el superhéroe más débil de género M
e- Determinar cuál es el superhéroe más débil de género NB
f- Determinar la fuerza promedio de los superhéroes de género NB
g- Determinar cuántos superhéroes tienen cada tipo de color de ojos.
h- Determinar cuántos superhéroes tienen cada tipo de color de pelo.
i- Listar todos los superhéroes agrupados por color de ojos.
j- Listar todos los superhéroes agrupados por tipo de inteligencia
k- Salir''' )

    opcion = input("Ingrese una opcion: ")

    if opcion == 'a':
        superheroe_nb (lista_personajes,'NB')

    elif opcion == 'b':
        obtener_heroe_mas_alto(lista_personajes,'F')
        print(f"El heroe mas alto es {obtener_heroe_mas_alto(lista_personajes,'F')}")

    elif opcion == 'c': 
        obtener_heroe_mas_alto(lista_personajes,'M')
        print(f"El heroe mas alto es {obtener_heroe_mas_alto(lista_personajes,'M')}")

    elif opcion == 'd':
        obtener_heroe_mas_debil(lista_personajes,'M')
        print(f"El heroe mas debil es {obtener_heroe_mas_debil(lista_personajes,'M')}")

    elif opcion == 'e':
        obtener_heroe_mas_debil(lista_personajes,'NB')
        print(f"El heroe mas debil es {obtener_heroe_mas_debil(lista_personajes,'NB')}")

    elif opcion == 'f':
        promedio_fuerzas_por_genero(lista_personajes,'NB')
        print(f"El promedio es:{promedio_fuerzas_por_genero(lista_personajes,'NB')}")

    elif opcion == 'g':
        puntos("color_ojos","cantidad")
        print("Color de ojos:\n{0}".format (puntos("color_ojos","cantidad")))

    elif opcion == 'h':
        puntos("color_pelo","cantidad")
        print("Color de pelo:\n{0}".format (puntos("color_pelo","cantidad")))

    elif opcion == 'i':
        puntos("color_ojos","agrupar")
        print("Segun su color de pelo:\n{0}".format(puntos("color_pelo","agrupar")))

    elif opcion == 'j':
        puntos("inteligencia","agrupar")
        print("Segun su inteligencia:\n{0}".format(puntos("inteligencia","agrupar")))

    elif opcion == 'k':
        break