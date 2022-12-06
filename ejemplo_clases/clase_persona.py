class Persona:
    def __init__(self, nombre="", edad=0):
        self.__nombre = nombre
        self.__edad = edad

    def Detalles(self):
        return f"Mi nombre es {self.__nombre} y tengo {self.__edad}"

    def __str__(self) -> str:
        return f"{self.__nombre} {self.__edad}"    

#mipersona = Persona("luis", 45)
#print(mipersona.Detalles())

class Trabajador(Persona):
    def __init__(self, nombre="", edad=0, salario=0.0):
        super().__init__(nombre, edad)
        self.__salario=salario

    def Detalles(self):
        return super(Trabajador, self).Detalles()+f" ,además tengo un salario de ${self.__salario}"

#mitrabajador=Trabajador("Luis", 45, 10000)
#print(mitrabajador.Detalles())

class Estudiante(Persona):
    def __init__(self, nombre="", edad=0, nivel=""):
        super(Estudiante, self).__init__(nombre, edad)
        self.__nivel=nivel

    def Detalles(self):
        return super(Estudiante, self).Detalles()+f" , estoy en el nivel {self.__nivel}"

class Estudiante_Trabajador(Trabajador, Estudiante):
    def __init__(self, nombre="", edad=0, nivel="", salario=0.0):
        super().__init__(nombre, edad, salario)

    def Detalles(self):
        super(Estudiante_Trabajador, self).Detalles()+f" Trabajo y Estudio"


#miestudiantetrabajador=Estudiante_Trabajador("Luis", 45, 500)
#print(miestudiantetrabajador.Detalles())
#print(isinstance(mipersona,Estudiante))