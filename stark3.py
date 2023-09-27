def stark_normalizar_datos(lista_personajes:list):
    resultado = False
    if lista_personajes == []:
        print("Error. Lista vacía")
        return False
    else:
        for personaje in lista_personajes:
            if type(personaje["altura"]) == float or type(personaje["peso"]) == float or type(personaje["fuerza"]) == int:
                print('''Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos 
ya no se hayan normalizado anteriormente''')
                return False
            else:
                personaje["altura"] = float(personaje["altura"])
                personaje["peso"] = float(personaje["peso"])
                personaje["fuerza"] = int(personaje["fuerza"])
                resultado = True
        if resultado == True:
            print("Datos normalizados")
    return True

def obtener_dato(heroe:dict,clave:str):
    if heroe == {}:
        return False
    dato = heroe[clave]
    return dato

def obtener_nombre(heroe:dict):
    if heroe == {}:
        return False
    nombre = heroe["nombre"]
    return "Nombre: {0}".format(nombre)

def obtener_nombre_y_dato(heroe:dict, clave:str):
    if heroe == {}:
        return False
    nombre = heroe["nombre"]
    dato = heroe[clave]

    return"Nombre: {0} | {1}: {2} ".format(nombre,clave,dato)

def obtener_maximo(lista_personajes:list, clave:str):
    if lista_personajes == [] and type(clave) != float and type(clave) != int:
        return False
    else:
        maximo = lista_personajes [0]
        for heroe in lista_personajes:
            if heroe[clave] > maximo [clave]:
                maximo = heroe

    return maximo ['nombre'], maximo [clave]

def obtener_minimo(lista_personajes:list, clave:str):
    if lista_personajes == [] and type(clave) != float and type(clave) != int:
        return False
    else:
        minimo = lista_personajes [0]
        for heroe in lista_personajes:
            if heroe[clave] < minimo [clave]:
                    minimo = heroe

    return minimo['nombre'], minimo[clave]


def obtener_dato_cantidad(lista_personajes:list,numero:int,clave:str): 
    lista_dato_cantidad = []
    if numero == 0:
        eleccion = obtener_minimo(lista_personajes, clave)

    elif numero == 1:
        eleccion = obtener_maximo(lista_personajes,clave)

    for heroe in lista_personajes:
        if heroe[clave] == eleccion[1] :
            lista_dato_cantidad.append(heroe['nombre'])
            lista_dato_cantidad.append(heroe[clave])

    return lista_dato_cantidad


def stark_imprimir_heroes(lista_personajes:list):
    if lista_personajes == []:
        return False
    else:
        return lista_personajes

def sumar_dato_heroe(lista_personajes:list,clave:str):
    suma = 0
    for heroes in lista_personajes:
        if heroes == {}:
            print("diccionario vacío")
            return False
        else:
                suma += heroes[clave] 
    return suma

def dividir(dividendo:int,divisor:int):
    if divisor == 0:
        return False
    else:
        resultado = dividendo / divisor
    return resultado

def calcular_promedio(lista_personajes:list,clave:str):
    suma = sumar_dato_heroe(lista_personajes,clave)
    divisor = len(lista_personajes)
    resultado = dividir(suma, divisor)
    return resultado

def mostrar_promedio_dato(lista_personajes:list,clave:str):
    if lista_personajes == []:
        return False
    for heroe in lista_personajes:
        if type(heroe [clave]) == int or type(heroe[clave]) == float:
            return calcular_promedio(lista_personajes,clave)
        else:
            return False

def validar_entero(numero:str):
    return numero.isdigit()


def imprimir_menu():
    print('''1- Normalizar datos 
2. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
3. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
4. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
5. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
6. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
7. Recorrer la lista y determinar la fuerza promedio de los superhéroes de
género NB
8. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
9. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
10. Listar todos los superhéroes agrupados por color de ojos.
11. Listar todos los superhéroes agrupados por tipo de inteligencia
12- Salir''')

def stark_menu_principal():
    imprimir_menu()
    opcion = input("Ingrese una opcion: ")
    validacion = validar_entero(opcion)

    if validacion == True:
        opcion = int(opcion)
        if opcion < 0 or opcion > 13:
            return False
    else:
        return False
    return opcion

def obtener_superheroes_por_genero(lista_personajes:list, genero:str):
    superheroes_genero = []
    for superheroe in lista_personajes:
        if superheroe["genero"] == genero:
            superheroes_genero.append(superheroe)
    return superheroes_genero

def puntos(clave:str, tipo:str):
    cantidad = {}
    lista = {}
    for heroe in lista_personajes: 
        valor = heroe[clave].capitalize()
        nombre = heroe["nombre"]
        if valor in cantidad:
            cantidad[valor] += 1
            lista[valor].append(nombre) 

        else:
            cantidad[valor] = 1
            lista[valor] = [nombre]  

    if tipo == "cantidad": 
        return cantidad
    
    elif tipo == "agrupar":
        return lista

def stark_marvel_app(lista_personajes:list):
    bandera = True
    bandera_2 = True
    normalizar = stark_normalizar_datos(lista_personajes)
    while bandera == True: 
        opcion = stark_menu_principal()
        while bandera_2 == True:
            if opcion != 1:
                print("Hace falta normalizar los datos")
                opcion = stark_menu_principal()
            else:
                stark_normalizar_datos(lista_personajes)
                bandera_2 = False
            
        if opcion == 2:
            heroe_por_genero = obtener_superheroes_por_genero(lista_personajes,'NB')
            stark_imprimir_heroes(heroe_por_genero)
            print(stark_imprimir_heroes(heroe_por_genero))

        elif opcion == 3:
            heroe_por_genero = obtener_superheroes_por_genero(lista_personajes,'F')
            obtener_maximo(heroe_por_genero, "altura")
            print(obtener_maximo(heroe_por_genero, "altura"))

        elif opcion == 4:
            heroe_por_genero = obtener_superheroes_por_genero(lista_personajes,'M')
            obtener_maximo(heroe_por_genero, "altura")
            print(obtener_maximo(heroe_por_genero, "altura"))

        elif opcion == 5:
            heroe_por_genero = obtener_superheroes_por_genero(lista_personajes,'M')
            obtener_minimo(heroe_por_genero, "fuerza")
            print(obtener_minimo(heroe_por_genero, "fuerza"))

        elif opcion == 6:
            heroe_por_genero = obtener_superheroes_por_genero(lista_personajes,'NB')
            obtener_minimo(heroe_por_genero, "fuerza")
            print(obtener_minimo(heroe_por_genero, "fuerza"))


        elif opcion == 7:
            heroe_por_genero = obtener_superheroes_por_genero(lista_personajes,'NB')
            calcular_promedio(heroe_por_genero,"fuerza")
            print(mostrar_promedio_dato(heroe_por_genero,"fuerza"))


        elif opcion == 8:
            pass

        elif opcion == 9:
            pass

        elif opcion == 10:
            pass

        elif opcion == 11:
            pass

        elif opcion == 12:
            bandera = False



from data_stark import lista_personajes



stark_marvel_app(lista_personajes)