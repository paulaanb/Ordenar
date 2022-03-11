# Ordenar
Este es el link del repositorio https://github.com/paulaanb/Ordenar

El código de los ejercicios son los siguientes:

```

#Codigo para Especificación de está_explorado
#Importamos las librerias y creamos una lista
import random

lista = []

#Definimos una funcion para crear una lista aleatoria
def creacion_lista():
    repe = random.randint(5, 15)
    for i in range(repe):
        num = random.randint(0, 10)
        lista.append(num)
    return lista


#Creamos una funcion para separar los segmentos
def segmentos(lista, i):
    segmento = []
    segmento.append(lista[i])
    while (len(lista) > 1) and (lista[i] >= lista[i + 1]):
        segmento.append(lista[i + 1])
        lista.pop(i + 1)
    lista.pop(i)
    return segmento


#Creamos una funcion para crear una lista con los segmentos de la lista anterior
def lista_segmento(lista, grupodeSegmentos):
    while len(lista) > 1:
        segmento = []
        segmento = segmentos(lista, 0)
        print(segmento)
        grupodeSegmentos.append(segmento)
        print(" La lista resultante es " + str(lista))
    return grupodeSegmentos
   
   
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

#Codigo para Ordenación topologica
#Definimos las tareas a realizar y las restricciones correspondientes
tareas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
restricciones = [(1, 3), (3, 5), (6, 8), (9, 12), (11, 12), (13, 15), ]
realizadas = []

#Creamos una funcion para comprobar cuales tareas tienen restricciones para añadirlas a una lista
def antecedentes(t):
    devolver = []
    for j in range(len(restricciones)):
        res = restricciones[j]
        if t == res[1]:
            devolver.append(res[0])
    return devolver

#Creamos otra funcion para comprobar si las funciones con restricciones se pueden realizar sin restricciones
def finalizadas(prec):
    excepciones = 0
    for i in range(len(prec)):
        if prec[i] in finalizadas(prec):
            excepciones = excepciones + 1
    if excepciones == len(prec):
        return True
    else:
        return False

#Mediante un bucle creamos el codigo principal para ejecutar el algoritmo
while len(finalizadas) < len(tareas):
    for i in range(len(tareas)):
        t = tareas[i]
        prec = antecedentes(t)
        if t not in finalizadas:
            if len(prec) == 0:
                finalizadas.append(t)
            elif finalizadas(prec) == True:
                realizadas.append(t)
#Ejecutamos el algotimo correspondiente
print(realizadas)
    

