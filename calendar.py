# creamos las variables de año y mes
año = int(input('Ingrese un año: '))
mes = int(input('Ingrese un mes [1-12]: '))
dia = int(input('ingrese un dia [1-31]: '))

if 1 <= mes <= 12 and 1 <= dia <= 31: # verificamos que los valores ingresado sean los permitidos
    if (año % 4 == 0) and (año % 100 != 0) and (año % 400):
        # tipo_año = 'biciesto' si se cumple la condicion anterior el año es biciesto
        # verificamos que mes es y si es el ultimo dia de dicho mes
        if mes == 2 and dia < 29:
            print('La fecha siguiente es [yyyy-mm-dd] {}-{}-{}'.format(año, mes, dia + 1)) # si es menor al ultimo dia se aumenta uno al dia
        elif (mes == 1 or mes == 3 or mes == 5 or mes == 6 or mes == 8 or mes == 10 or mes == 12) and dia < 31:
            print('La fecha siguiente es [yyyy-mm-dd] {}-{}-{}'.format(año, mes, dia + 1))
        elif (mes == 4 or mes == 7 or mes == 9 or mes == 11) and dia < 30:
            print('La fecha siguiente es [yyyy-mm-dd] {}-{}-{}'.format(año, mes, dia + 1))
        else:
            # si en algun mes el dia es el ultimo, se pasa al primer dia del siguiente mes
            print('La fecha siguiente es [yyyy-mm-dd] {}-{}-{}'.format(año, mes + 1, 1))

    else:
        # tipo_año = 'no_biciesto'
        if mes == 2 and dia < 28:
            print('La fecha siguiente es [yyyy-mm-dd] {}-{}-{}'.format(año, mes, dia + 1))
        elif (mes == 1 or mes == 3 or mes == 5 or mes == 6 or mes == 8 or mes == 10 or mes == 12) and dia < 31:
            print('La fecha siguiente es [yyyy-mm-dd] {}-{}-{}'.format(año, mes, dia + 1))
        elif (mes == 4 or mes == 7 or mes == 9 or mes == 11) and dia < 30:
            print('La fecha siguiente es [yyyy-mm-dd] {}-{}-{}'.format(año, mes, dia + 1))
        else:
            print('La fecha siguiente es [yyyy-mm-dd] {}-{}-{}'.format(año, mes + 1, 1))

else:
    print('Mes o dia mal ingresados')
