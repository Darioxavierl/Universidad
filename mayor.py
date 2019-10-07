# Ingrese su código aquí
#definimos los numeros
num1 = 12
num2 = 4
num3 = 5
num4 = 43

lista = [num1, num2, num3, num4]

i = 0

for numero in lista:
    if numero < lista[i + 1]:
        mayor = lista[i + 1]
    else:
        mayor = numero
    i += 1