print("===== Listas =====")

Lista = ["k1", "k2", "k3", "k4", "k5", "k6"]
print ("===== Los salones del edificio K son los siguientes: ======\n")
print(Lista)

#Insertando datos a la lista
Lista.insert(0, "k6")
Lista.insert(1, "k5")
Lista.insert(2, "k4")
Lista.insert(3, "k3")
Lista.insert(4, "k2")
Lista.insert(5, "k1")

print ("\n======Lista con los nuevos valores: ======\n")
print(Lista)

print("\n =====Mandar a traer los datos===== \n")
print("Primer Elemento: ")
print(Lista[1])
print("Los primeros 5: ")
print(Lista[0:5])
print("Primer Elemento: ")
print(Lista[:])
print("Primer Elemento: ")
print(Lista[:2])
print("Primer Elemento: ")
print(Lista[5:])

print("\n===== Invierte los datos de la lista =====\n")
Lista.reverse()
print(Lista)

print("\n===== Datos duplicados =====")
print(Lista.count("k4"))

Lista.remove("k3")
print(Lista)

print("\n===== Devolver la posicion =====")
print(Lista.index("k5"))

print("\n===== Datos que contiene la lista ======")
print(Lista)

print("\n ======= Datos Ordenados en la lista ======")
Lista.sort()
print(Lista)