
#Sobre valores de las horas
horas_normales = 40
valor_hora = 8
extra_por_hora = 1.5
valor_hora_extra = valor_hora * extra_por_hora
sueldo = 0

horas_trabajadas = int(input('Horas tabajadas este mes: '))

if horas_trabajadas <= horas_normales:
    sueldo = horas_trabajadas * valor_hora
    print('El sueldo del mes es: {}'.format(sueldo))
else:
    horas_extra = horas_trabajadas - horas_normales
    sueldo = (horas_normales * valor_hora) + (horas_extra * valor_hora_extra)
    print('El sueldo del mes es: {}'.format(sueldo))


