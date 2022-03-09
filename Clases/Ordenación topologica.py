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