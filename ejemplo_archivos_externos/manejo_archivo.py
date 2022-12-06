#from io import open

#archivo_texto=open("archivo.txt", "w")
#frase="Estoy estudiando python \n por un curso"
#archivo_texto.write(frase)
#archivo_texto.close()
#archivo_texto=open("archivo.txt", "a")
#archivo_texto.write("\n otra linea")
#archivo_texto.close()
#archivo_texto=open("archivo.txt", "r")
#texto_archivo=archivo_texto.read()
#print(texto_archivo)
#archivo_texto.close()
#archivo_texto=open("archivo.txt", "r")
#archivo_texto.seek(12)
#print(archivo_texto.read(15))
#archivo_texto.close()
archivo=open("archivo.txt", "r+") #lectura y escritura 
texto=archivo.readlines()
cantlineas=len(texto)
for l in texto:
    print(l)
archivo.write("\n esta es otra prueba")  

archivo.close()
