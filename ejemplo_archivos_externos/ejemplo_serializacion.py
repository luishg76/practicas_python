import pickle
lista_nombres=["Luis", "Onel","Ana"]
binario=open("fichero_binario","wb")#escritura binaria
pickle.dump(lista_nombres, binario)
binario.close()
del(binario)
binario=open("fichero_binario", "rb")#lectura binaria
objeto=pickle.load(binario)
binario.close()