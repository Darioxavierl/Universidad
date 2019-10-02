#definimos que estaciones se toman en cuenta
estacion_1 = 'primavera'
estacion_2 = 'verano'
estacion_3 = 'otoño'
estacion_4 = 'invierno'

# la estacion y medicion que se quiere analizar
estacion_actual = 'otoño'
temperatura_medida = 75

#cada estacion tiene sus propios valores donde se define un rango normal, anormal, o muy anormal
if estacion_actual == estacion_1:
    if 0 <= temperatura_medida <= 75:
        print('Rango normal')
    elif temperatura_medida <= 75:
        print('Anormal')
    else:
        print('Muy anormal')

elif estacion_actual == estacion_2:
    if 0 <= temperatura_medida <= 100:
        print('Rango normal')
    elif temperatura_medida <= 200:
        print('Anormal')
    else:
        print('Muy anormal')

elif estacion_actual == estacion_3:
    if 0 <= temperatura_medida <= 60:
        print('Rango normal')
    elif temperatura_medida <= 60:
        print('Anormal')
    else:
        print('Muy anormal')

elif estacion_actual == estacion_4:
    if 0 <= temperatura_medida <= 40:
        print('Rango normal')
    elif temperatura_medida <= 40:
        print('Anormal')
    else:
        print('Muy anormal')