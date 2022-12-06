#import modulos.funciones_matematicas as mfm
#from modulos.funciones_matematicas import suma
from pck_calculo.funciones_matematicas import *
from pck_calculo.funciones_estadisticos import *
from ejemplo_clases.clase_persona import *

mipersona=Persona("Luis", 45)
print(mipersona.Detalles())
print(suma(12,6))
print(promedio([4,4,3,5,3,5]))