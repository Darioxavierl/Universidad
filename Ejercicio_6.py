
# preguntamos que transformacion quiere hacer el usuario

transformacion = input('En que grados esta la temperatura que quiere transformar? (Celcius / Farenheit)' ).upper()


if transformacion == 'CELCIUS':
    temperatura = int(input('Cuantos grados Celcius? '))  # si los grados son celcius procede a preguntar cuantos grados son
    temperatura_transformada = ((9/5)*temperatura) + 32   # realiza la transformacion
    print('{}°C es {}° en Farenheit'.format(temperatura, temperatura_transformada))  # imprime el resultado

if transformacion == 'FARENHEIT':
    temperatura = int(input('Cuantos grados Farenheit? '))  # si los grados son farenheit procede a preguntar cuantos grados son
    temperatura_transformada = (5/9) * (temperatura - 32)  # realiza la transformacion
    print('{}°F es {}° en Celsius'.format(temperatura, temperatura_transformada))  # imprime el resultado

