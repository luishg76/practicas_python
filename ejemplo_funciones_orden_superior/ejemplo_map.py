def increment_porciento(num):
    return num+(num*0.25)

lst_numeros=[17,24,7,18,26,19]

#print(list(map(increment_porciento,lst_numeros)))

print(list(map(lambda x: x+(x*0.25),lst_numeros)))