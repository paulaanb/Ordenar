#Codigo para Ordenación por inserción dicotómica
#Importamos las librerias y creamos la lista para hacer posteriormente la tabla
import random
lista = []

#Ahora creamos una tabla aleatoria para calcular el resultado solicitado
def creacion_lista():
    r = random.randint(1, 50)
    for i in range(r):
        num = random.randint(0, 25)
        lista.append(num)
    return lista


#Definimos la funcion para ordenar la lista mediante  insercion dicotomica
def ordenar_lista(lista, i):
    posicion = 0
    if i < len(lista):
        posicion = lista[i]
        lista.pop(i)
        if posicion >= lista[i - 1]:
            lista.insert(i, posicion)
        else:
            lista.insert(i - 1, posicion)
            if lista[i - 2] >= lista[i - 1] and i > 1:
                ordenar_lista(lista, i - 1)
            else:
                ordenar_lista(lista, i)
    else:
        return lista
    ordenar_lista(lista, i + 1)
    return lista


#Creamos las ordenes para ejecutar el codigo
creacion_lista()
print(lista)
ordenar_lista(lista, 0)
print(lista)


