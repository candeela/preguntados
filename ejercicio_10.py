'''
Candela Kevarkian
Pedir al usuario que ingrese los datos de 5 alumnos y guardarlos en sus
respectivas listas. Validar el ingreso de datos según su criterio.
Datos:
nombre, sexo (f/m), nota (validar).
Una vez cargados los datos:
Mostrar el nombre del hombre con nota más baja
Mostrar el promedio de notas de las mujeres'''

lista_nombres = [ ] 
lista_sexo = [ ]
lista_nota = [ ]
acumulador = 0 
contador = 0 
nota_baja = 0


for i in range(5): 
    nombre = str(input("Ingrese su nombre"))
    lista_nombres.append(nombre)

    sexo = str(input("Ingrese su sexo"))
    while sexo != 'f' and sexo != 'm':
        sexo = str(input("Reingrese su sexo"))
    lista_sexo.append(sexo)

    nota = int(input("Ingrese su nota"))
    while nota >10 or nota <0:
        nota = int(input("Reingrese su nota"))
    lista_nota.append(nota)

for i in lista_nota: 
    if lista_sexo [i]  == 'm':
        if nota_baja == 0:
            nota_baja = lista_nota[i] 
            bandera = False
        
        if nota_baja > lista_nota [ i] :
            nota_baja = nota_baja = lista_nota[i] 



promedio = acumulador / contador

print(f"El hombre con la nota mas baja es {nota_baja}")