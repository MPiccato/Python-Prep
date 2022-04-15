class Matematica:
    def __init__(self,listNum):
        self.lista = listNum

    def numPrimo(self, numPrimo):
        esPrimo = True
        for i in range(2,numPrimo):
            if numPrimo % i == 0:
                esPrimo = False
                break
        return esPrimo

    def extraePrimos(self):
        listPrimos = []
        for nro in self.lista:

            if nro > 1:
                if self.numPrimo(int(nro)):
                    listPrimos.append(nro)
            else:
                continue
        return listPrimos
        
    def cambioGrados(self,valor, origen,destino):
        diccambioGrados={}
        # De Celsius a Farenhait

        deCelsiusaF = (valor * 9/5) + 32

        diccambioGrados['De Celsius a F'] = deCelsiusaF

        # De Celsius a Kevin

        deCelsiusaK = valor + 273.15

        diccambioGrados['De Celsius a K'] = deCelsiusaK

        # De Kevin a Celsius

        deKaCelsius = deCelsiusaK - 273.15

        diccambioGrados['De K a Celsius'] = deKaCelsius

        # De Farenhait a Celsius

        deFaCelsius = (deCelsiusaF - 32) / (9/5)
        diccambioGrados['De F a Celsius'] = deFaCelsius

        print(diccambioGrados)

        if origen == 'C':        
            if destino == 'K':
                return deCelsiusaK
            if destino == 'F':
                return deCelsiusaF

    def factorial(self,numero):
        if(type(numero) != int):
            return 'El número debe ser un entero'

        if (numero < 0):
            return 'El número debe ser positivo'
        if (numero > 1):
            numero = numero * self.factorial(numero - 1)
        
        return numero