from data_stark import lista_personajes
import funciones_stark2

def obtener_superheroes_por_genero(lista_personajes:list, genero:str):
    superheroes_genero = []
    for superheroe in lista_personajes:
        if superheroe["genero"] == genero:
            superheroes_genero.append(superheroe)
    return superheroes_genero

def obtener_heroe_mas_alto(lista_personajes:list, genero:str):
    superheroes_genero = obtener_superheroes_por_genero(lista_personajes, genero)
    heroe_mas_alto = superheroes_genero[0]
    for superheroe in superheroes_genero:
        if float(superheroe["altura"]) > float(heroe_mas_alto["altura"]):
            heroe_mas_alto = superheroe
    return heroe_mas_alto

def obtener_heroe_mas_debil(lista_personajes:list, genero:str):
    superheroes_genero = obtener_superheroes_por_genero(lista_personajes, genero)
    heroe_mas_debil = superheroes_genero[0]
    for superheroe in superheroes_genero:
        if int(superheroe["fuerza"]) < int(heroe_mas_debil["fuerza"]):
            heroe_mas_debil = superheroe
    return heroe_mas_debil



def obtener_fuerza_promedio(lista_personajes:list, genero:str):
    superheroes_genero = obtener_superheroes_por_genero(lista_personajes, genero)
    total_fuerza = sum(float(superheroe["fuerza"]) for superheroe in superheroes)
    return total_fuerza / len(superheroes_genero)

def contar_color_ojos(lista_personajes):
    color_ojos_counts = {}
    for superheroe in lista_personajes:
        color_ojos = superheroe["color_ojos"]
        if color_ojos in color_ojos_counts:
            color_ojos_counts[color_ojos] += 1
        else:
            color_ojos_counts[color_ojos] = 1
    return color_ojos_counts

def contar_color_pelo(lista_personajes):
    color_pelo_counts = {}
    for superheroe in lista_personajes:
        color_pelo = superheroe["color_pelo"]
        if color_pelo in color_pelo_counts:
            color_pelo_counts[color_pelo] += 1
        else:
            color_pelo_counts[color_pelo] = 1
    return color_pelo_counts

def listar_superheroes_por_color_ojos(lista_personajes):
    superheroes_por_color_ojos = {}
    for superheroe in lista_personajes:
        color_ojos = superheroe["color_ojos"]
        if color_ojos in superheroes_por_color_ojos:
            superheroes_por_color_ojos[color_ojos].append(superheroe)
        else:
            superheroes_por_color_ojos[color_ojos] = [superheroe]
    return superheroes_por_color_ojos

def listar_superheroes_por_tipo_inteligencia(lista_personajes):
    superheroes_por_tipo_inteligencia = {}
    for superheroe in lista_personajes:
        tipo_inteligencia = superheroe["inteligencia"]
        if tipo_inteligencia in superheroes_por_tipo_inteligencia:
            superheroes_por_tipo_inteligencia[tipo_inteligencia].append(superheroe)
        else:
            superheroes_por_tipo_inteligencia[tipo_inteligencia] = [superheroe]
    return superheroes_por_tipo_inteligencia

while True:
    print('''
\na. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
\nb. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
\nc. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
\nd. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
\ne. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
\nf. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB
\ng. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
\nh. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
\ni. Listar todos los superhéroes agrupados por color de ojos.
\nj. Listar todos los superhéroes agrupados por tipo de inteligencia
\nk. Salir''')

    opcion = input("Ingrese una opción: ")

    if opcion == 'a':
        funciones_stark2.nombres_heroes_nb(lista_personajes)

    elif opcion == 'b':
        heroe_mas_alto_f = obtener_heroe_mas_alto(lista_personajes, 'F')
        print(f"El superhéroe más alto de género F es: {heroe_mas_alto_f['nombre']}")


    elif opcion == 'c':
        heroe_mas_alto_m = obtener_heroe_mas_alto(lista_personajes, 'M')
        if heroe_mas_alto_m:
            print(f"El superhéroe más alto de género M es: {heroe_mas_alto_m['nombre']}")
        else:
            print("No hay superhéroes de género M.")



    elif opcion == 'd':
        heroe_mas_debil_m = obtener_heroe_mas_debil(lista_personajes, 'M')
        if heroe_mas_debil_m:
            print(f"El superhéroe más débil de género M es: {heroe_mas_debil_m['nombre']}")
        else:
            print("No hay superhéroes de género M.")

    elif opcion == 'e':
        heroe_mas_debil_nb = obtener_heroe_mas_debil(lista_personajes, 'NB')
        if heroe_mas_debil_nb:
            print(f"El superhéroe más débil de género NB es: {heroe_mas_debil_nb['nombre']}")
        else:
            print("No hay superhéroes de género NB.")

    elif opcion == 'f':
        fuerza_promedio_nb = obtener_fuerza_promedio_nb(lista_personajes)
        print(f"La fuerza promedio de los superhéroes de género NB es: {fuerza_promedio_nb}")

    elif opcion == 'g':
        color_ojos_counts = contar_color_ojos(lista_personajes)
        for color, count in color_ojos_counts.items():
            print(f"Color de ojos: {color}, Cantidad: {count}")

    elif opcion == 'h':
        color_pelo_counts = contar_color_pelo(lista_personajes)
        for color, count in color_pelo_counts.items():
            print(f"Color de pelo: {color}, Cantidad: {count}")

    elif opcion == 'i':
        superheroes_por_color_ojos = listar_superheroes_por_color_ojos(lista_personajes)
        for color, superheroes in superheroes_por_color_ojos.items():
            print(f"Color de ojos: {color}")
            for superheroe in superheroes:
                print(f"- {superheroe['nombre']}")

    elif opcion == 'j':
        superheroes_por_tipo_inteligencia = listar_superheroes_por_tipo_inteligencia(lista_personajes)
        for tipo, superheroes in superheroes_por_tipo_inteligencia.items():
            print(f"Tipo de inteligencia: {tipo}")
            for superheroe in superheroes:
                print(f"- {superheroe['nombre']}")



    elif opcion == 'k':
        break