import pickle
from ejemplo_clases.clase_persona import Persona

mipersona1 = Persona("luis", 45)
mipersona2 = Persona("onel", 45)
mipersona3 = Persona("ana", 25)

personas=[mipersona1, mipersona2, mipersona3]

fichero=open("personas","wb")

pickle.dump(personas,fichero)

fichero.close()

del(fichero)

fichero=open("personas","rb")
listapersonas=pickle.load(fichero)
fichero.close()
for p in listapersonas:
    print(p.Detalles())



