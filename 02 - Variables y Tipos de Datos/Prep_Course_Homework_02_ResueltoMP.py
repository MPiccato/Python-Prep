import math
#Resolución de los ejercicios MPiccato

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
num_entero = 12
print(num_entero)

# 2) Imprimir el tipo de dato de la constante 8.5
const = 8.5
print(type(const))
print(type(8.5))

# 3) Imprimir el tipo de dato de la variable creada en el punto 1
print(type(num_entero))

# 4) Crear una variable que contenga tu nombre
nombre = 'Martin Piccato'

# 5) Crear una variable que contenga un número complejo
num_complex = 4 + 3j

# 6) Mostrar el tipo de dato de la variable crada en el punto 5
print(type(num_complex))

# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
num_Py = math.pi
print("{0:.4f}".format(float(num_Py)))
print(round(num_Py,4))

# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
primer_bool = True
segundo_bool = True
print(primer_bool and segundo_bool)

# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8
print(type(primer_bool))
print(type(segundo_bool))

# 10) Asignar a una variable, la suma de un número entero y otro decimal
suma = 2 + 2.4

# 11) Realizar una operación de suma de números complejos
suma_complex = 2 + 4j

# 12) Realizar una operación de suma de un número real y otro complejo
suma_complex2 = 2.4 + 4j


# 13) Realizar una operación de multiplicación
multiplicar = 2 * 2

# 14) Mostrar el resultado de elevar 2 a la octava potencia
potencia = 2 ** 8
print("Potencia:", potencia)


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
cociente = 27 / 4
print(cociente)

# 16) De la división anterior solamente mostrar la parte entera
parte_entera = 27//4
print(parte_entera)

# 17) De la división de 27 entre 4 mostrar solamente el resto
print(27 % 4)

# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
print(6*4+3)
# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
print('hola ' + 'martin')

# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
print("2" == 2)

# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
print (int("2") == 2)

# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
a = float('3.8')
b = '3,8'
b.replace(',','.')
print(b)

# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
variable = 3
variable -= 1
print(variable)

# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
print(1<<2)

# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
# Porque no se puede sumar un entero con una cadena

# 26) Realizar una operación válida entre valores de tipo entero y string
print(int('2') + 2)
