año = int(input('Ingrese un año: '))

ultimo_dia_30 = 30
ultimo_dia_31 = 31
ultimo_dia_28 = 28
ultimo_dia_29 = 29

if (año % 4 == 0) and (año % 100 != 0) and (año % 400):
    tipo_año = 'biciesto'
    mes = int(input('Ingrese un mes [1-12]: '))
    dia = int(input('ingrese un dia [1-31]: '))
    if tipo_año == 'biciesto':
        if mes == 2 and dia == ultimo_dia_28:
            print('{} {} {}'.format(año, mes + 1, 1))
        else:
            print('{} {} {}'.format(año, mes, dia + 1))
else:
    tipo_año = 'no_biciesto'

