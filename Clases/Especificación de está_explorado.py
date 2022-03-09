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


#Terminamos de crear el codigo para ejecutar el algoritmo solicitado
creacion_lista()
print(lista)
grupodeSegmentos = []
grupodeSegmentos = lista_segmento(lista, grupodeSegmentos)(lista, grupodeSegmentos)
print(grupodeSegmentos)
