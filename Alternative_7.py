x = int(input("Ingrese el valor de x "))

# definimos los contadores
menores_input = 0
mayores_input = 0
igual_input = 0

# números previamente almacenados
num1 = 10
num2 = 5
num3 = 4
num4 = 6
num5 = 3

# almacenamos en una lista los numeros
lista = [num1, num2, num3, num4, num5]

# con un loop comparamos cada entrada de la lista con el valor ingresado
for item in lista:
    if item != x:
        if item < x:
            menores_input += 1
        elif item > x:
            mayores_input += 1
    else:
        igual_input += 1

# imprime los resultados
print('Existen {} numero(s) mayores a x, {} numero(s) menores a x y {} numero(s) iguales a x'.format(mayores_input, menores_input, igual_input))