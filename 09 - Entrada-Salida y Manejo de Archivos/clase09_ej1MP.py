import sys
if (len(sys.argv) == 4):
    print('El primer parámetro es:', sys.argv[1])
    print('El segundo parámetro es:', sys.argv[2])
    print('El tercer parámetro es:', sys.argv[3])
else:
    print('ERROR: no introdujo la cantidad de parámetros necesaria')
    