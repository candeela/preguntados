def stark_normalizar_datos(heroes):
    """
    Normaliza los datos numéricos en la lista de héroes.
    
    Args:
    - heroes (list): Lista de diccionarios que representan héroes.

    Returns:
    - bool: True si los datos se normalizaron con éxito, False en caso contrario.
    """
    if not heroes:
        return False
    
    datos_normalizados = False

    for heroe in heroes:
        for clave, valor in heroe.items():
            if isinstance(valor, str) and valor.isnumeric():
                heroe[clave] = int(valor)
                datos_normalizados = True
            elif isinstance(valor, str) and valor.replace(".", "").isnumeric():
                heroe[clave] = float(valor)
                datos_normalizados = True

    return datos_normalizados

def obtener_dato(heroe, clave):
    """
    Obtiene un dato específico de un héroe.

    Args:
    - heroe (dict): Diccionario que representa a un héroe.
    - clave (str): Clave del dato a obtener.

    Returns:
    - Valor del dato si existe, False en caso contrario.
    """
    if not heroe or "nombre" not in heroe:
        return False

    return heroe.get(clave, False)

def obtener_nombre(heroe):
    """
    Obtiene el nombre formateado de un héroe.

    Args:
    - heroe (dict): Diccionario que representa a un héroe.

    Returns:
    - str: Nombre formateado o False si no existe un nombre en el héroe.
    """
    nombre = obtener_dato(heroe, "nombre")
    if nombre:
        return f"Nombre: {nombre}"
    return False

def obtener_nombre_y_dato(heroe, clave):
    """
    Obtiene el nombre y un dato específico de un héroe.

    Args:
    - heroe (dict): Diccionario que representa a un héroe.
    - clave (str): Clave del dato a obtener.

    Returns:
    - str: Nombre y dato formateado o False si no existe un nombre o dato en el héroe.
    """
    nombre = obtener_nombre(heroe)
    dato = obtener_dato(heroe, clave)
    
    if nombre and dato is not False:
        return f"{nombre} | {clave}: {dato}"
    return False

def obtener_maximo(heroes, clave):
    """
    Obtiene el valor máximo de una clave específica entre los héroes.

    Args:
    - heroes (list): Lista de diccionarios que representan héroes.
    - clave (str): Clave del dato a buscar.

    Returns:
    - Valor máximo encontrado o False si no se encuentra el dato o la lista está vacía.
    """
    if not heroes:
        return False

    max_valor = None

    for heroe in heroes:
        valor = obtener_dato(heroe, clave)
        if isinstance(valor, (int, float)):
            if max_valor is None or valor > max_valor:
                max_valor = valor

    return max_valor

def obtener_minimo(heroes, clave):
    """
    Obtiene el valor mínimo de una clave específica entre los héroes.

    Args:
    - heroes (list): Lista de diccionarios que representan héroes.
    - clave (str): Clave del dato a buscar.

    Returns:
    - Valor mínimo encontrado o False si no se encuentra el dato o la lista está vacía.
    """
    if not heroes:
        return False

    min_valor = None

    for heroe in heroes:
        valor = obtener_dato(heroe, clave)
        if isinstance(valor, (int, float)):
            if min_valor is None or valor < min_valor:
                min_valor = valor

    return min_valor

def obtener_dato_cantidad(heroes, valor, clave):
    """
    Obtiene la lista de héroes que tienen un dato específico y clave específicos.

    Args:
    - heroes (list): Lista de diccionarios que representan héroes.
    - valor (float or int): Valor a buscar en el dato especificado.
    - clave (str): Clave del dato a buscar.

    Returns:
    - list: Lista de héroes que cumplen con la condición.
    """
    if not heroes:
        return []

    resultado = []

    for heroe in heroes:
        heroe_valor = obtener_dato(heroe, clave)
        if heroe_valor == valor:
            resultado.append(heroe)

    return resultado

def stark_imprimir_heroes(heroes):
    """
    Imprime la información completa de los héroes en la lista.

    Args:
    - heroes (list): Lista de diccionarios que representan héroes.
    """
    if not heroes:
        return False

    for heroe in heroes:
        print(heroe)

def sumar_dato_heroe(heroes, clave):
    """
    Suma un dato específico de todos los héroes en la lista.

    Args:
    - heroes (list): Lista de diccionarios que representan héroes.
    - clave (str): Clave del dato a sumar.

    Returns:
    - float or int: Suma de los datos o False si la lista está vacía o el dato no es numérico.
    """
    if not heroes:
        return False

    suma = 0

    for heroe in heroes:
        valor = obtener_dato(heroe, clave)
        if isinstance(valor, (int, float)):
            suma += valor

    return suma

def dividir(dividendo, divisor):
    """
    Realiza la división entre dos números.

    Args:
    - dividendo (float or int): Número a dividir.
    - divisor (float or int): Número por el cual se dividirá el dividendo.

    Returns:
    - float: Resultado de la división o False si el divisor es 0.
    """
    if divisor == 0:
        return False

    return dividendo / divisor

def calcular_promedio(heroes, clave):
    """
    Calcula el promedio de un dato específico entre los héroes en la lista.

    Args:
    - heroes (list): Lista de diccionarios que representan héroes.
    - clave (str): Clave del dato a promediar.

    Returns:
    - float: Promedio del dato o False si la lista está vacía o el dato no es numérico.
    """
    if not heroes:
        return False

    suma = sumar_dato_heroe(heroes, clave)
    cantidad_heroes = len(heroes)

    if suma is not False and cantidad_heroes > 0:
        return suma / cantidad_heroes

    return False

def mostrar_promedio_dato(heroes, clave):
    """
    Muestra el promedio de un dato específico entre los héroes en la lista.

    Args:
    - heroes (list): Lista de diccionarios que representan héroes.
    - clave (str): Clave del dato a promediar.

    Returns:
    - str: Mensaje con el promedio o False si la lista está vacía o el dato no es numérico.
    """
    promedio = calcular_promedio(heroes, clave)

    if promedio is not False:
        return f"Promedio de {clave}: {promedio}"
    
    return False

def imprimir_menu():
    """
    Imprime el menú de opciones por pantalla.
    """
    print("Menú:")
    print("1. Normalizar datos")
    print("2. Recorrer la lista imprimiendo nombres de superhéroes de género NB")
    print("3. Recorrer la lista y determinar el superhéroe más alto de género F")
    print("4. Recorrer la lista y determinar el superhéroe más alto de género M")
    print("5. Recorrer la lista y determinar el superhéroe más débil de género M")
    print("6. Recorrer la lista y determinar el superhéroe más débil de género NB")
    print("7. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB")
    print("8. Determinar cuántos superhéroes tienen cada tipo de color de ojos.")
    print("9. Determinar cuántos superhéroes tienen cada tipo de color de pelo.")
    print("10. Listar todos los superhéroes agrupados por color de ojos.")
    print("11. Listar todos los superhéroes agrupados por tipo de inteligencia.")
    print("0. Salir")

def validar_entero(numero_str):
    """
    Valida si un string es un número entero.

    Args:
    - numero_str (str): String que se desea validar.

    Returns:
    - bool: True si el string es un número entero, False en caso contrario.
    """
    return numero_str.isdigit()

def stark_menu_principal(lista_heroes):
    """
    Imprime el menú principal y solicita una opción al usuario.

    Args:
    - lista_heroes (list): Lista de diccionarios que representan héroes.

    Returns:
    - int: Opción seleccionada por el usuario.
    """
    while True:
        imprimir_menu()
        opcion = input("Seleccione una opción: ")

        if validar_entero(opcion):
            opcion = int(opcion)
            if opcion >= 0 and opcion <= 11:
                return opcion
            else:
                print("Opción inválida. Intente nuevamente.")
        else:
            print("Opción inválida. Intente nuevamente.")

def stark_marvel_app(lista_heroes):
    """
    Función principal que ejecuta el programa Stark Marvel.

    Args:
    - lista_heroes (list): Lista de diccionarios que representan héroes.
    """
    datos_normalizados = False

    while True:
        opcion = stark_menu_principal(lista_heroes)

        if opcion == 1:
            if not datos_normalizados:
                datos_normalizados = stark_normalizar_datos(lista_heroes)
                if datos_normalizados:
                    print("Datos Normalizados")
                else:
                    print("Hubo un error al normalizar los datos. Verifique que la lista no esté vacía o que los datos ya no se hayan normalizado anteriormente")
            else:
                print("Los datos ya han sido normalizados anteriormente.")
        elif opcion == 2:
            # Recorrer la lista imprimiendo nombres de superhéroes de género NB
            for heroe in lista_heroes:
                genero = obtener_dato(heroe, "genero")
                if genero == "NB":
                    print(obtener_nombre(heroe))
        elif opcion == 3:
            # Recorrer la lista y determinar el superhéroe más alto de género F
            max_altura_f = obtener_maximo([heroe for heroe in lista_heroes if obtener_dato(heroe, "genero") == "F"], "altura")
            if max_altura_f is not False:
                heroes_altura_max_f = obtener_dato_cantidad(lista_heroes, max_altura_f, "altura")
                print("Superhéroes más altos de género F:")
                stark_imprimir_heroes(heroes_altura_max_f)
            else:
                print("No hay superhéroes de género F en la lista.")
        elif opcion == 4:
            # Recorrer la lista y determinar el superhéroe más alto de género M
            max_altura_m = obtener_maximo([heroe for heroe in lista_heroes if obtener_dato(heroe, "genero") == "M"], "altura")
            if max_altura_m is not False:
                heroes_altura_max_m = obtener_dato_cantidad(lista_heroes, max_altura_m, "altura")
                print("Superhéroes más altos de género M:")
                stark_imprimir_heroes(heroes_altura_max_m)
            else:
                print("No hay superhéroes de género M en la lista.")
        elif opcion == 5:
            # Recorrer la lista y determinar el superhéroe más débil de género M
            min_fuerza_m = obtener_minimo([heroe for heroe in lista_heroes if obtener_dato(heroe, "genero") == "M"], "fuerza")
            if min_fuerza_m is not False:
                heroes_fuerza_min_m = obtener_dato_cantidad(lista_heroes, min_fuerza_m, "fuerza")
                print("Superhéroes más débiles de género M:")
                stark_imprimir_heroes(heroes_fuerza_min_m)
            else:
                print("No hay superhéroes de género M en la lista.")
        elif opcion == 6:
            # Recorrer la lista y determinar el superhéroe más débil de género NB
            min_fuerza_nb = obtener_minimo([heroe for heroe in lista_heroes if obtener_dato(heroe, "genero") == "NB"], "fuerza")
            if min_fuerza_nb is not False:
                heroes_fuerza_min_nb = obtener_dato_cantidad(lista_heroes, min_fuerza_nb, "fuerza")
                print("Superhéroes más débiles de género NB:")
                stark_imprimir_heroes(heroes_fuerza_min_nb)
            else:
                print("No hay superhéroes de género NB en la lista.")
        elif opcion == 7:
            # Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB
            promedio_fuerza_nb = calcular_promedio([heroe for heroe in lista_heroes if obtener_dato(heroe, "genero") == "NB"], "fuerza")
            if promedio_fuerza_nb is not False:
                print(f"Fuerza promedio de superhéroes de género NB: {promedio_fuerza_nb}")
            else:
                print("No hay superhéroes de género NB en la lista.")
        elif opcion == 8:
            # Determinar cuántos superhéroes tienen cada tipo de color de ojos
            resultado_colores_ojos = {}
            for heroe in lista_heroes:
                color_ojos = obtener_dato(heroe, "color_de_ojos")
                if color_ojos:
                    if color_ojos in resultado_colores_ojos:
                        resultado_colores_ojos[color_ojos] += 1
                    else:
                        resultado_colores_ojos[color_ojos] = 1

            print("Cantidad de superhéroes por tipo de color de ojos:")
            for color, cantidad in resultado_colores_ojos.items():
                print(f"{color}: {cantidad}")
        elif opcion == 9:
            # Determinar cuántos superhéroes tienen cada tipo de color de pelo
            resultado_colores_pelo = {}
            for heroe in lista_heroes:
                color_pelo = obtener_dato(heroe, "color_de_pelo")
                if color_pelo:
                    if color_pelo in resultado_colores_pelo:
                        resultado_colores_pelo[color_pelo] += 1
                    else:
                        resultado_colores_pelo[color_pelo] = 1

            print("Cantidad de superhéroes por tipo de color de pelo:")
            for color, cantidad in resultado_colores_pelo.items():
                print(f"{color}: {cantidad}")
        elif opcion == 10:
            # Listar todos los superhéroes agrupados por color de ojos
            resultado_colores_ojos = {}
            for heroe in lista_heroes:
                color_ojos = obtener_dato(heroe, "color_de_ojos")
                if color_ojos:
                    if color_ojos in resultado_colores_ojos:
                        resultado_colores_ojos[color_ojos].append(obtener_nombre(heroe))
                    else:
                        resultado_colores_ojos[color_ojos] = [obtener_nombre(heroe)]

            print("Superhéroes agrupados por color de ojos:")
            for color, heroes in resultado_colores_ojos.items():
                print(f"{color}:")
                for heroe in heroes:
                    print(f"- {heroe}")
        elif opcion == 11:
            # Listar todos los superhéroes agrupados por tipo de inteligencia
            resultado_inteligencia = {}
            for heroe in lista_heroes:
                inteligencia = obtener_dato(heroe, "inteligencia")
                if inteligencia:
                    if inteligencia in resultado_inteligencia:
                        resultado_inteligencia[inteligencia].append(obtener_nombre(heroe))
                    else:
                        resultado_inteligencia[inteligencia] = [obtener_nombre(heroe)]

            print("Superhéroes agrupados por tipo de inteligencia:")
            for inteligencia, heroes in resultado_inteligencia.items():
                print(f"{inteligencia}:")
                for heroe in heroes:
                    print(f"- {heroe}")
        elif opcion == 0:
            break

# Ejemplo de uso
if __name__ == "__main__":
    lista_heroes = [...]  # Tu lista de héroes aquí
    stark_marvel_app(lista_heroes)
