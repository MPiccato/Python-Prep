import os
import sys

montañas = {'nombre':[  'Everest','K2','Kanchenjunga','Lhotse','Makalu',
                        'Cho Oyu','Dhaulagiri','Manaslu','Nanga Parbat','Annapurna I'],
            'orden':[1,2,3,4,5,6,7,8,9,10],
            'cordillera':['Himalaya','Karakórum','Himalaya','Himalaya','Himalaya'
                        ,'Himalaya','Himalaya','Himalaya','Karakórum','Himalaya'],
            'pais': ['Nepal','Pakistán','Nepal','Nepal','Nepal','Nepal','Nepal','Nepal',
                    'Pakistán','Nepal'],
            'altura':[8849,8611,8586,8516,8485,8188,8167,8163,8125,8091]}

# VOY A TOMAR LAS KEYS Y ESCRIBIRLAS EN EL ARCHIVO.
archivo = open('clase09_ej3.csv', 'w')
for clave in montañas.keys():
    if (clave == 'altura'):
        archivo.write(clave+'\n')
    else:
        archivo.write(clave+',')

#agregando los valores por columnas y lineas
ind = 0
while (ind < 10):
    archivo.write(montañas['nombre'][ind]+',')
    archivo.write(str(montañas['orden'][ind])+',')
    archivo.write(montañas['cordillera'][ind]+',')
    archivo.write(montañas['pais'][ind]+',')
    archivo.write(str(montañas['altura'][ind])+'\n')
    ind += 1

###---- Desarrollado conforme lo que yo creo-----

"""
for i in range(0,10):
    archivo.write('\n')
    for indice in montañas.keys():
        linea = str(list((indice + ':', montañas[indice][i])))
        archivo.write(linea)

"""        
archivo.close() 