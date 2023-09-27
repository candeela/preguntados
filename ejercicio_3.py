'''
Candela Kevarkian

Ingresar 5 números enteros, distintos de cero.

Informar:
a. Cantidad de pares e impares.lis
b. El menor número ingresado.lis
c. De los pares el mayor número ingresado.
d. Suma de los positivos. LIS
e. Producto de los negativos.list'''

acumulador_positivos = 0 
acumulador_negativos = 1
contador = 0 
contador_pares = 0
contador_impares = 0
bandera_1 = True
bandera_2 = True

while contador < 5:
    numero =  input ("Ingrese un numero entero, distinto de cero")
    numero = int(numero)
    while numero == 0:
        numero =  input ("Reingrese  un numero entero, distinto de cero")
        numero = int(numero) 
    contador = contador + 1

#cantidad de pares
    if numero % 2 == 0:
        contador_pares += 1 

        #maximo par
        if bandera_1 == True:
            maximo = numero
            bandera_1 = False

        if numero > maximo:
            maximo = numero

    #cantidad impares
    else:
        contador_impares += 1


    #minimo numero 
    if bandera_2 == True: 
        menor = numero
        bandera_2 = False

    if numero < menor:
        menor = numero

    #suma de los positivos
    if numero > 0 :
        acumulador_positivos = acumulador_positivos + numero

    #producto de los negativos
    if numero < 0:
        acumulador_negativos = acumulador_negativos * numero 

mensaje = f'''
    La cantidad de pares es: {contador_pares} \n
    La cantidad de impares es: {contador_impares}\n
    El menor número ingresado es : {menor}\n
    El mayor número par ingresado es: {maximo}\n
    La suma de los positivos es : {acumulador_positivos} \n
    El producto de los negativos es : {acumulador_negativos} \n
'''

print(mensaje)
