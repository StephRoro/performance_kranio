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




# 2
# Requerir al usuario que ingrese un número entero e informar si es primo o no, 
# utilizando una función booleana que lo decida.




# 3
# Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, al finalizar, 
# la cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.


# 4
# Escribir la función titulo(), la cual recibe un string y lo retorna convirtiendo la primera letra de cada #
# palabra a mayúscula y las demás letras a minúscula, dejando inalterados los demás caracteres. 
# Precondición: el separador de palabras es el espacio: " ". 
# Agregar doctests con suficientes casos de prueba para validar que la función retorna el valor esperado ante distintos argumentos.
