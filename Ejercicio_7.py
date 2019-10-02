
x = int(input("Ingrese el valor de x: "))

# números previamente almacenados
num1 = 10
num2 = 5
num3 = 4
num4 = 6
num5 = 3

# definimos los contadores
iguales_a_input = 0
mayores_a_input = 0
menores_a_input = 0

# comparamos el numero ingresado con cada numero almacenado
if x != num1:
    if x < num1:
        mayores_a_input += 1  # si el numero ingresado es menor el contador suma uno, se repite con el resto de numeros
    elif x > num1:
        menores_a_input += 1  # si el numero ingresado es mayor el contador suma uno, se repite con el resto de numeros
else:
    iguales_a_input +=1  # si el numero ingresado es igual el contador suma uno, se repite con el resto de numeros

if x != num2:
    if x < num2:
        mayores_a_input += 1
    elif x > num2:
        menores_a_input += 1
else:
    iguales_a_input +=1

if x != num3:
    if x < num3:
        mayores_a_input += 1
    elif x > num3:
        menores_a_input += 1
else:
    iguales_a_input +=1

if x != num4:
    if x < num4:
        mayores_a_input += 1
    elif x > num4:
        menores_a_input += 1
else:
    iguales_a_input +=1

if x != num5:
    if x < num5:
        mayores_a_input += 1
    elif x > num5:
        menores_a_input += 1
else:
    iguales_a_input +=1

# imprime el total de los numeros, mayores, menores e iguales
print('Existen {} numero(s) mayores a x, {} numero(s) menores a x y {} numero(s) iguales a x'.format(mayores_a_input, menores_a_input, iguales_a_input))