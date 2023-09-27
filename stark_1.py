'''
Candela Kevarkian

A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor
fuerza (MÁXIMO)
C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
(MÍNIMO)
D. Recorrer la lista y determinar el peso promedio de los superhéroes
masculinos (PROMEDIO)
E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
género) los cuales su fuerza supere a la fuerza promedio de todas las
superhéroes de género femenino
'''

from data_stark import lista_personajes

while True:
    print('''a-Imprimir por consola todos los datos de cada superhéroe
\n b- Mostrar la identidad y el peso del superhéroe con mayor fuerza 
\n c- Mostrar nombre e identidad del superhéroe más bajo 
\n d-Determinar el peso promedio de los superhéroes masculinos 
\n e-mostrar nombre y peso de los superhéroes los cuales su fuerza supere a la fuerza promedio de todas las 
superhéroes de género femenino 
\n f- Salir''' )
    opcion = input("Ingrese una opcion: ")

    if opcion == 'a':
        for personajes in lista_personajes: 
            nombre = personajes["nombre"]
            identidad = personajes["identidad"]
            empresa = personajes["empresa"]
            altura = personajes["altura"]
            peso = personajes["peso"]
            genero = personajes["genero"]
            color_ojos = personajes["color_ojos"]
            color_pelo = personajes["color_pelo"]
            fuerza = personajes["fuerza"]
            inteligencia = personajes["inteligencia"]

            print(f"Personaje - {nombre} , {identidad} , {empresa} , {altura} , {peso} , {genero} , {color_ojos} , {color_ojos} , {fuerza} , {inteligencia}")

    elif opcion == 'b':
        #B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)
        fuerza = lista_personajes[0]["fuerza"]
        fuerza_maximo = int(fuerza)
        id_maximo = lista_personajes[0]["identidad"]
        peso_maximo = lista_personajes[0] ["peso"]

        for personajes in lista_personajes:
            if int(personajes["fuerza"]) > fuerza_maximo:
                    fuerza_maximo = int(personajes["fuerza"])
                    id_maximo = personajes["identidad"]
                    peso_maximo = personajes["peso"]

        print(f"La identidad del personaje es :{id_maximo} y su peso es: {peso_maximo}")


    elif opcion == 'c':
        #. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
        altura = lista_personajes[0]["altura"]
        altura_minimo = float(altura)
        nombre_minimo = lista_personajes[0] ["nombre"]
        id_minimo = lista_personajes[0]["identidad"]

        for personajes in lista_personajes:
            if float(personajes["altura"]) < altura_minimo:
                    altura_minimo = float(personajes["altura"])
                    id_minimo = personajes["identidad"]
                    nombre_minimo = personajes["nombre"]

        print(f"La identidad del personaje es :{id_minimo} y su nombre es: {nombre_minimo}")


    elif opcion == 'd':
        acumulador_m = 0 
        contador_m = 0
        
        #D. Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)
        for personajes in lista_personajes:
            if personajes ["genero"] == 'M':
                contador_m = contador_m + 1
                peso_hombre = personajes ["peso"]
                peso_hombre = float(peso_hombre)
                acumulador_m = acumulador_m + peso_hombre

        if contador_m != 0 :
            promedio = acumulador_m / contador_m

            print(f"El peso promedio de los superhéroes masculinos es: {promedio} ")

        else: 
            print("No se pudo calcular el promedio")




    elif opcion == 'e':
#mostrar nombre y peso de los superhéroes (cualquiergénero) los cuales su fuerza supere a la fuerza promedio de todas lassuperhéroes de género femenino
        acumulador_f = 0
        contador_f = 0  

        for personajes in lista_personajes:
            if personajes ["genero"] == 'F':
                contador_f = contador_f + 1
                fuerza_mujer = personajes ["fuerza"]
                fuerza_mujer = float(fuerza_mujer)
                acumulador_f = acumulador_f + fuerza_mujer
                
        if contador_f != 0:
            promedio_f = acumulador_f / contador_f
            for personajes in lista_personajes:
                if int(personajes["fuerza"]) > promedio_f:
                    print(f"El nombre es: {personajes['nombre']} y su peso es:  {personajes['peso']}")

        else: 
            print("No hay se puede calcular el promedio")

    elif opcion == 'f':
        break