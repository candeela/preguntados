'''A. Analizar detenidamente el set de datos.

B. Recorrer la lista guardando en sub-listas: la pregunta, cada opción y la respuesta
correcta. 

C. Crear 2 botones (rectángulos) uno con la etiqueta “Pregunta”, otro con la etiqueta
“Reiniciar”

D. Imprimir el Score: 999 donde se va a ir acumulando el puntaje de las respuestas
correctas. Cada respuesta correcta suma 10 puntos. 

E. Al hacer clic en el botón (rectángulo) “Pregunta” debe mostrar las preguntas
comenzando por la primera y las tres opciones, cada clic en este botón pasa a la
siguiente pregunta.

F. Al hacer clic en una de las tres palabras que representa una de las tres opciones, si es
correcta, debe sumar el score y dejar de mostrar las opciones. 

G. Solo tiene 2 opciones para acertar la respuesta correcta y sumar puntos, si agotó ambas
opciones, deja de mostrar las opciones y no suma score

H. Al hacer clic en el botón (rectángulo) “Reiniciar” debe mostrar las preguntas
comenzando por la primera y las tres opciones, cada clic pasa a la siguiente pregunta.
También debe reiniciar el Score. '''

import pygame
from constantes import *
from datos import lista

lista_preguntas = [] 
lista_opcion_a = []
lista_opcion_b = []
lista_opcion_c = []
lista_correcta = []
pregunta = ""
opcion_a = ""
opcion_b = ""
opcion_c = ""
posicion = 0
puntos = 0


#guardar cada elemento en una lista
for e_lista in lista:
    lista_preguntas.append(e_lista['pregunta'])
    lista_opcion_a.append(e_lista['a'])
    lista_opcion_b.append(e_lista['b'])
    lista_opcion_c.append(e_lista['c'])
    lista_correcta.append(e_lista['correcta'])


pygame.init()
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Preguntados")

imagen = pygame.image.load("preguntados.png")
imagen = pygame.transform.scale(imagen,(80,80))
sonido_1 = pygame.mixer.Sound("correcto.mp3")
sonido_2 = pygame.mixer.Sound("incorrecto.mp3")
fuente = pygame.font.SysFont("Arial", 25)
texto_preguntas = fuente.render(str(pregunta),True, COLOR_GRIS)
texto_pregunta = fuente.render("Pregunta",True, COLOR_GRIS)
texto_reiniciar = fuente.render("Reiniciar",True, COLOR_GRIS)
texto_score = fuente.render("Score: ",True, COLOR_GRIS)
texto_opcion_a = fuente.render(str(opcion_a),True, COLOR_GRIS)
texto_opcion_b = fuente.render(str(opcion_b),True, COLOR_GRIS)
texto_opcion_c = fuente.render(str(opcion_c),True, COLOR_GRIS)
texto_puntos = fuente.render(str(puntos),True, COLOR_GRIS)


flag_ejecutar = True

while flag_ejecutar: 

    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_ejecutar = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos)
            print(posicion_click)

            #boton de preguntas
            if posicion_click[0] > 18 and posicion_click[0] < 216 and posicion_click[1] > 450 and posicion_click[1] < 550:
                if posicion == len(lista_preguntas) - 1:
                    posicion = 0

                else:
                    pregunta = lista_preguntas[posicion]
                    opcion_a = lista_opcion_a[posicion]
                    opcion_b = lista_opcion_b[posicion]
                    opcion_c = lista_opcion_c[posicion]
                    texto_preguntas = fuente.render(str(pregunta),True, COLOR_GRIS)
                    texto_opcion_a = fuente.render('a) ' + str(opcion_a),True, COLOR_GRIS)
                    texto_opcion_b = fuente.render('b) ' + str(opcion_b),True, COLOR_GRIS)
                    texto_opcion_c = fuente.render('c) ' + str(opcion_c),True, COLOR_GRIS)
                    chances = 2
                    print(chances)
                    posicion = posicion + 1




            #boton de reiniciar
            if posicion_click[0] > 580 and posicion_click[0] < 780 and posicion_click[1] > 450 and posicion_click[1] < 550:
                pregunta = lista_preguntas[0]
                opcion_a = lista_opcion_a[0]
                opcion_b = lista_opcion_b[0]
                opcion_c = lista_opcion_c[0]
                texto_preguntas = fuente.render(str(pregunta),True, COLOR_GRIS)
                texto_opcion_a = fuente.render('a) ' + str(opcion_a),True, COLOR_GRIS)
                texto_opcion_b = fuente.render('b)'  + str(opcion_b),True, COLOR_GRIS)
                texto_opcion_c = fuente.render('c) ' + str(opcion_c),True, COLOR_GRIS)
                puntos = 0
                texto_puntos = fuente.render(str(puntos),True, COLOR_GRIS)
                chances = 2
                posicion = 0
                print(chances)



            #opcion a 
            if posicion_click[0] > 37 and posicion_click[0] < 186 and posicion_click[1] > 300 and posicion_click[1] < 326:
                if lista_correcta[posicion - 1] == 'a' :
                    puntos += 10
                    texto_puntos = fuente.render(str(puntos),True, COLOR_GRIS)
                    texto_opcion_a = fuente.render('a) ' + str(opcion_a),True, COLOR_VERDE_CLARO)
                    texto_opcion_b = fuente.render(' ' ,True, COLOR_GRIS)
                    texto_opcion_c = fuente.render(' ' ,True, COLOR_GRIS)
                    sonido_1.play()
                    chances = 2
                    print(chances)

                else: 
                    chances = chances - 1
                    texto_opcion_a = fuente.render(' ' ,True, COLOR_GRIS)
                    sonido_2.play()
                    print(chances)

            #opcion b
            if posicion_click[0] > 297 and posicion_click[0] < 470 and posicion_click[1] > 300 and posicion_click[1] < 326:
                if lista_correcta[posicion - 1] == 'b' :
                    puntos += 10
                    texto_puntos = fuente.render(str(puntos),True, COLOR_GRIS)
                    texto_opcion_b = fuente.render('b) ' + str(opcion_b),True, COLOR_VERDE_CLARO)
                    texto_opcion_a = fuente.render(' ' ,True, COLOR_GRIS)
                    texto_opcion_c = fuente.render(' ' ,True, COLOR_GRIS)
                    sonido_1.play()
                    chances = 2
                    print(chances)

                else: 
                    chances = chances - 1
                    texto_opcion_b = fuente.render(''  ,True, COLOR_GRIS)
                    sonido_2.play()
                    print(chances)


            #opcion c
            if posicion_click[0] > 568 and posicion_click[0] < 778 and posicion_click[1] > 300 and posicion_click[1] < 326:
                if lista_correcta[posicion - 1] == 'c' :
                    puntos += 10 
                    texto_puntos = fuente.render(str(puntos),True, COLOR_GRIS)
                    texto_opcion_c = fuente.render('c) ' + str(opcion_c),True, COLOR_VERDE_CLARO)
                    texto_opcion_a = fuente.render(' ' ,True, COLOR_GRIS)
                    texto_opcion_b = fuente.render(' ' ,True, COLOR_GRIS)
                    sonido_1.play()
                    chances = 2
                    print(chances)

                else: 
                    chances = chances - 1
                    texto_opcion_c = fuente.render(' ' ,True, COLOR_GRIS)
                    sonido_2.play()
                    print(chances)


            if chances <= 0:
                texto_opcion_a = fuente.render(' ' ,True, COLOR_GRIS)
                texto_opcion_b = fuente.render(''  ,True, COLOR_GRIS)
                texto_opcion_c = fuente.render(' ' ,True, COLOR_GRIS)





    pantalla.fill(COLOR_ROSA)
    pygame.draw.rect(pantalla, COLOR_BLANCO, (580,450,200,100))
    pygame.draw.rect(pantalla, COLOR_BLANCO, (18,450,200,100))


    pantalla.blit(imagen,(20,50),)
    pantalla.blit(texto_preguntas,(150,170))
    pantalla.blit(texto_pregunta,(48,480))
    pantalla.blit(texto_opcion_a,(40,300))
    pantalla.blit(texto_opcion_b,(300,300))
    pantalla.blit(texto_opcion_c,(565,300))
    pantalla.blit(texto_reiniciar,(620,480))
    pantalla.blit(texto_score,(200,50))
    pantalla.blit(texto_puntos,(280,50))


    pygame.display.flip()

pygame.quit()