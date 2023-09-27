
def contar_color(lista_personajes:list, tipo:str):
    color_counts = {}
    for superheroe in lista_personajes:
        color = superheroe[tipo]
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1
    return color_counts