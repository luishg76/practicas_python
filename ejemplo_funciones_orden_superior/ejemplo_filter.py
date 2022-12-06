def es_par(num):
    if num%2==0:
        return True

lst_numeros=[17,24,7,18,26,19]

#print(list(filter(es_par,lst_numeros)))

#utilizando lambda
print(list(filter(lambda x: x % 2 == 0,lst_numeros)))
