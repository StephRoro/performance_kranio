############################################ Variables y tipos de dato ########################################################

# 1
# Escriba un programa que solicite al usuario que ingrese su nombre. 
# El nombre se debe almacenar en una variable llamada nombre. 
# A continuación se debe mostrar en pantalla el texto “Ahora estás en la matrix, [usuario]”, donde “[usuario]” 
# se reemplazará por el nombre que el usuario haya ingresado.}

nombre = input("Por favor, ingresa tu nombre: ")
print(f"Ahora estás en la matrix, {nombre}!")


# 2
# Escriba un programa que solicite al usuario un número y le reste el 15%, almacenando todo en una única variable. 
# A continuación, mostrar el resultado final en pantalla.

numero = float(input("Por favor, ingresa un número: "))
resultado = numero - (numero * 0.15)
print(f"El resultado después de aplicar un descuento del 15% es: {resultado}")


# 3
# Escribí un programa para solicitar al usuario el ingreso de un número entero y que luego imprima un valor de verdad 
# dependiendo de si el número es par o no. Recordar que un número es par si el resto, al dividirlo por 2, es 0.

numero = int(input("Por favor, ingresa un número entero: "))
es_par = numero % 2 == 0

if es_par:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} no es par.")



# 4
# Escribí un programa que le pida al usuario ingresar dos palabras y las guarde en dos variables, 
# y que luego imprima True si la primera palabra es menor que la segunda o False si no lo es.

palabra1 = input("Por favor, ingresa la primera palabra: ")
palabra2 = input("Ahora, ingresa la segunda palabra: ")

es_menor = palabra1 < palabra2

if es_menor:
    print(True)
else:
    print(False)

############################################ Funciones y modulos ########################################################

# 1
# Solicitar al usuario que ingrese su dirección email. 
# Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. 
# Una dirección se considerará válida si contiene el símbolo "@".

def es_direccion_valida(email):
    if "@" in email:
        return True
    else:
        return False

direccion_email = input("Ingrese su dirección de correo electrónico: ")
if es_direccion_valida(direccion_email):
    print("La dirección de correo electrónico es válida.")
else:
    print("La dirección de correo electrónico no es válida.")


# 2
# Requerir al usuario que ingrese un número entero e informar si es primo o no, 
# utilizando una función booleana que lo decida.

def es_primo(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
numero = int(input("Ingrese un numero: "))
if es_primo(numero):
    print("el numero es primo.")
else:
    print("el numero no es primo.")


# 3
# Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, al finalizar, 
# la cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.


def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

def num(numero):
    return len(str(numero))

numero = int(input("Entroduzca un numero: "))
resultado = factorial(numero)
cantidad_digitos = num(resultado)

print(f"Numero: {numero}")
print(f"Factorial: {resultado}")
print(f"Cantidad de dígitos en el factorial: {cantidad_digitos}")


# 4
# Escribir la función titulo(), la cual recibe un string y lo retorna convirtiendo la primera letra de cada #
# palabra a mayúscula y las demás letras a minúscula, dejando inalterados los demás caracteres. 
# Precondición: el separador de palabras es el espacio: " ". 
# Agregar doctests con suficientes casos de prueba para validar que la función retorna el valor esperado ante distintos argumentos.

def titulo(cadena):
    palabras = cadena.split()
    palabras = [palabra[0].upper() + palabra[1:] for palabra in palabras]
    return " ".join(palabras)

#Pruebas con doctests
def prueba_titulo():
    """
    >>> titulo("esto es una prueba")
    'Esto es Una Prueba'
    >>> titulo("hola MUndo")
    'Hola Mundo'
    >>> titulo("OTRO EJEMPLO") 
    'Otro Ejemplo'
    >>> titulo("mayusculas")
    'Mayusculas'
    """
    pass

if __name__ == "__main":
    import doctest
    doctest.testmod()
    
# escribir este commando para ejecutar doctest
# python3 -m doctest fundamentos_en_python.py -v


############################################ Estructuras de Datos ########################################################

# A) Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. Finalizar al ingresar el número 0, el cual no debe guardarse.
numeros = []
while True:
    numero = int(input("Ingrese un número (0 para finalizar): "))
    if numero == 0:
        break
    numeros.append(numero)

# B) Solicitar al usuario que ingrese un número y eliminar la primera ocurrencia si existe.
numero_a_eliminar = int(input("Ingrese el número que desea eliminar:"))
if numero_a_eliminar in numeros:
    numeros.remove(numero_a_eliminar)
else:
    print("El número no se encuentra en la lista.")

# C) Recorrer la lista para imprimir la sumatoria de todos los elementos.
suma = sum(numeros)
print("La sumatoria de todos los elementos es:", suma)

# D) Solicitar al usuario otro número y crear una lista con los elementos menores que el número dado.
numero_limite = int(input("Ingrese un número límite: "))
numeros_menores = [num for num in numeros if num < numero_limite]
print("Elementos menores que", numero_limite, ":", numeros_menores)

# E) Generar e imprimir una nueva lista que contenga tuplas con los números y sus frecuencias.
frecuencias = {}
for numero in numeros:
    if numero in frecuencias:
        frecuencias[numero] += 1
    else:
        frecuencias[numero] = 1

tuplas_frecuencias = [(numero, frecuencia) for numero, frecuencia in frecuencias.items()]
print("Tuplas de números y sus frecuencias:", tuplas_frecuencias)
