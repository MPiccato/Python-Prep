import sys
import os
import datetime

if (len(sys.argv) == 2):
    fecha_tiempo = datetime.datetime.now()
    fecha_tiempo = int(datetime.datetime.timestamp(fecha_tiempo))

    lluvia = sys.argv[1]
    temperatura = input('Ingrese la temperatura en grados centígrados: ')
    humedad = input('Ingrese el porcentaje de humedad: ')
    linea = str(fecha_tiempo) + ',' + temperatura + ',' + humedad + ',' + lluvia

    archivo_lluvia = open('clase09_ej2.csv', 'a')
    archivo_lluvia.write(linea + '\n')
    archivo_lluvia.close()
else:
    print('Error: no ontridujo todos los parámetros esperados')
    