
variable= int(input("Por favor, seleccione el ejercicio que desea ejecutar (1-3):"))
if variable==1:
  import Ejercicio1
if variable ==2:
  import Ejercicio2
if variable ==3:
  import Ejercicio3
else:
  print("Por favor, eliga uno de los tres ejercicios disponibles.")

from Clases.Ejercicio1 import *
from Clases.Ejercicio2 import *
from Clases.Ejercicio3 import *

if __name__ == 