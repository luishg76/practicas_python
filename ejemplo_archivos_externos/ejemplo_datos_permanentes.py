import pickle
from ejemplo_clases.clase_persona import Persona

class Repo_Personas:
    
    def __init__(self):
        self.personas=[]
        ficheroExt=open("ficheroExt","ab+")
        ficheroExt.seek(0)
        try:
            self.personas=pickle.load(ficheroExt)
            print(f"Se cargaron correctamente {len(self.personas)}")
        except:
            print("La Lista de personas está vacia")
        finally:
            ficheroExt.close()
            del(ficheroExt)

    def agregar(self, persona):
        self.personas.append(persona)

    def detalles(self):
        for d in self.personas:
            print(d)
    
miLista=Repo_Personas()
miLista.agregar(Persona("Luis", 45))
miLista.agregar(Persona("Onel", 45))
miLista.agregar(Persona("Ana", 25))

#miLista.detalles()
