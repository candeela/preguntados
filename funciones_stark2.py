from data_stark import lista_personajes
def obtener_superheroes_por_genero(lista_personajes:list, genero:str):
    superheroes_genero = []
    for superheroe in lista_personajes:
        if superheroe["genero"] == genero:
            superheroes_genero.append(superheroe)
    return superheroes_genero

def superheroe_nb(lista_personajes:list,genero:str):
    superheroes_nb = obtener_superheroes_por_genero(lista_personajes, genero)
    for superheroe in superheroes_nb:
        print(superheroe["nombre"])
    return 

def obtener_heroe_mas_alto(lista_personajes:list, genero:str):
    superheroes_genero = obtener_superheroes_por_genero(lista_personajes, genero)
    heroe_mas_alto = superheroes_genero[0]
    for superheroe in superheroes_genero:
        if float(superheroe["altura"]) > float(heroe_mas_alto["altura"]):
            heroe_mas_alto = superheroe
    return heroe_mas_alto['nombre']

def obtener_heroe_mas_debil(lista_personajes:list, genero:str):
    superheroes_genero = obtener_superheroes_por_genero(lista_personajes, genero)
    heroe_mas_debil= superheroes_genero[0]
    for superheroe in superheroes_genero:
        if float(superheroe["fuerza"]) < float(heroe_mas_debil["fuerza"]):
            heroe_mas_debil = superheroe
    return heroe_mas_debil['nombre']

def promedio_fuerzas_por_genero (lista_personajes:list,genero:str):
    superheroes_genero = obtener_superheroes_por_genero(lista_personajes, genero)
    lista_fuerzas = []
    for superheroe in superheroes_genero:
        fuerza = int(superheroe['fuerza'])
        lista_fuerzas.append(fuerza)
        acumulador_fuerzas = 0

        for valor in lista_fuerzas: 
            acumulador_fuerzas += valor

        if len(lista_fuerzas) > 0:
            promedio = acumulador_fuerzas /len(lista_fuerzas)

    return promedio


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
            lista[valor] = [nombre]  # Crea una lista con el nombre como primer elemento

    if tipo == "cantidad": 
        return cantidad
    
    elif tipo == "agrupar":
        return lista