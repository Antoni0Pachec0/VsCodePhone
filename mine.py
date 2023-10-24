#Se crea una lista vacia
lista = []

#=============================================================================================
def insertar():
    tamaño = int(input("Ingrese el tamaño de la lista: "))
    
    for i in range(0, tamaño):
        dato = input("Digite un numero para ingresar a la lista: ")
        lista.insert(i, dato)

#=============================================================================================
def mostrar():
    print("Los elementos de la lista son: ", * lista)

#=============================================================================================
def agregar():
    indice = int(input("Ingrese el indice donde desea agregar: "))

    if(indice > len(lista) or indice < 0):
        print("El indice debe estar entre 0 y ", len(lista))
    else:
        elemento = int(input("Digite el elemento a agregar: "))
        
        lista.insert(indice,elemento)
        print("El elemento se ha insertado")

#=============================================================================================
def modificar():
    indice = int(input("Digite el indice del elemento a modificar: "))

    if(indice > len(lista) or indice < 0):
        print("El indice debe estar entre 0 y ", len(lista) -1)
    else:
        elemento = input("Digite el valor del elemento: ")
        
        lista[indice] = elemento
        print("Elemento modificado")

#=============================================================================================
def eliminar():
    indice = int(input("Digite el indice del elemento a eliminar: "))
    
    if(indice > len(lista) or indice < 0):
        print("El indice debe estar entre 0 y ", len(lista) -1)
    else:
        del lista[indice]
        print("Elemeto eliminado")
        
#=============================================================================================
opcion = 1

while(opcion > 0 and opcion < 6):
    print("\n*** Operaciones en la estructura de datos lista ***")
    print("""
    1.- Definir el tamaño inicial de la lista
    2.- Mostrar datos de la lista 
    3.- Agregar un nuevo dato a la lista 
    4.- Modificar un dato de la lista
    5.- Eliminar
    6.- Terminar el programa
    """)

    opcion = int(input("Elija una opcion: "))
    
    if(opcion == 1):
        insertar()
    elif(opcion == 2):
        mostrar()
    elif(opcion == 3):
        agregar()
    elif(opcion == 4):
        modificar()
    elif(opcion == 5):
        eliminar()
    elif(opcion == 6):
        print("Programa terminado")
    else:
        print("Opcion incorrecta")
