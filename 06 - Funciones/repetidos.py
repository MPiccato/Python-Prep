def minimoMaximo(diccionario, cantMinimo):
    cantMinimo = min(diccionario.keys(), key = lambda k: diccionario[k])
    return cantMinimo
def cantRepetidos(listaNum):
    repetidos = []
    totalNum = []

    for num in listaNum:
        if num not in totalNum:
            totalNum.append(num)
        else:

            repetidos.append(num)
    
    cantVecesNum={}

    for numero in repetidos:
        cantVecesNum[numero] = listaNum.count(numero)

    #Calculo minimo repetidos
    cantMinimo = min(cantVecesNum.keys(), key= lambda k: cantVecesNum[k])
 
 
    
        
    print(cantVecesNum)
    cantidadMax = max(cantVecesNum)
    if (len(cantVecesNum)>1):
        print('Los números que más se repiten son: {}'.format(cantVecesNum)) 
    #print('El número que más se repite es {} y lo hace {} veces'.format(cantidadMax,cantVecesNum[cantidadMax]))
    print ('El número que más se repite es el {} y lo hace {} veces'.format(cantidadMax,cantVecesNum[cantidadMax]))
  

cantRepetidos([1,2,3,3,5,5,5,5])