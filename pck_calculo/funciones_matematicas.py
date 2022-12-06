def suma(num1, num2):
    return num1+num2
def resta(num1, num2):
    return num1-num2
def multiplicacion(num1, num2):
    return num1*num2
def division(dividendo, divisor):
    try:
        return dividendo/divisor
    except ZeroDivisionError:
        return -1
        
     
    