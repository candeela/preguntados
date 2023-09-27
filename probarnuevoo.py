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
        eleccion = obtener_minimo(lista_personajes,clave)

    elif numero == 1:
        eleccion = obtener_maximo(lista_personajes, clave)

    for heroe in lista_personajes:
        if heroe[clave] == eleccion[1] :
            lista_dato_cantidad.append(heroe['nombre'])
            lista_dato_cantidad.append(heroe[clave])

    return lista_dato_cantidad


from data_stark import lista_personajes

while True:
    o=input('h: ')
    if o == 'a':
        obtener_dato_cantidad(lista_personajes,1,"fuerza")
        print(obtener_dato_cantidad(lista_personajes,1,"fuerza")) 