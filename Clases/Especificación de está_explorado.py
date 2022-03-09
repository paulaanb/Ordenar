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


#hacemos una funcion que separa un segmento
def segmentos(lista, i):
    segmento = []
    segmento.append(lista[i])
    while (len(lista) > 1) and (lista[i] >= lista[i + 1]):
        segmento.append(lista[i + 1])
        lista.pop(i + 1)
    lista.pop(i)
    return segmento


#funcion que hace una lista con todos los segmentos de la lista
def seg_lista(lista, grupoSegmentos):
    while len(lista) > 1:
        segmento = []
        segmento = segmentos(lista, 0)
        print(segmento)
        grupoSegmentos.append(segmento)
        print(" Esta es la lista que queda " + str(lista))
    return grupoSegmentos


#codigo principal
creacion_lista()
print(lista)
grupoSegmentos = []
grupoSegmentos = seg_lista(lista, grupoSegmentos)
print(grupoSegmentos)
