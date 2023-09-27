'''La división de higiene está trabajando en un control de stock para productos sanitarios.
Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe
obtener los siguientes datos:
1. El tipo (validar "barbijo", "jabón" o "alcohol")
2. El precio: (validar entre 100 y 300)
3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000
unidades)
4. La marca y el Fabricante.
Se debe informar lo siguiente:

A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
B. Del ítem con más unidades, el fabricante.
C. Cuántas unidades de jabones hay en total.'''


lista_productos = []


barbijo_caro = 0 

for i in range(5):

    tipo = str(input("Ingrese el tipo"))
    while tipo != "barbijo" and tipo != "jabon" and tipo != "alcohol":
        tipo = str(input("Reingrese el tipo"))

    precio = int(input("Ingrese el precio"))
    while precio > 300 or precio < 100:
        precio = int(input("Reingrese el precio"))

    cantidad = int(input("Ingrese la cantidad de unidades"))
    while cantidad > 1000 or cantidad <= 0 :
        cantidad = int(input("Reingrese la cantidad de unidades"))

    marca = str(input("Ingrese la marca y el fabricante"))


    lista_productos.append({"Tipo": tipo ,"Precio" : precio , "Cantidad" : cantidad , "Marca y fabricante" : marca })


for i in lista_productos:
    if tipo[i] == "barbijo":
        pass


