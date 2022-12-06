#minombre=input("Introduce tu nombre: ")
#print(f"Mi nombre es: {minombre.upper()}")
#print(f"Mi nombre es: {minombre.capitalize()}")
#print(f"Mi nombre es: {minombre.lower()}")

#validar
edad=input("Entre la edad: ")
while edad.isalpha():
    print("Entre un valor númerico")
    edad = input("Entre la edad: ")

if int(edad) < 18:
   print("Menor de edad")
else:
   print("Mayor de edad")



