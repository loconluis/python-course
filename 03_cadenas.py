from string import printable


name = "Luis" # Una forma de declarar una cadena
name2 = 'Juan' # Otra forma de declarar una cadena
name3 = '''Pedro''' # Otra forma de declarar una cadena pero multilinea

# las cadenas tambien tienen indices
cadena = "Hola Mundo"
print(cadena[0]) # H
print(cadena[1]) # o
print(cadena[2]) # l
print(cadena[3]) # a
print(cadena[4]) #
print(cadena[5]) # M
print(cadena[6]) # u
print(cadena[7]) # n
print(cadena[8]) # d
print(cadena[9]) # o


# asi mismo tienen longitud
print(len(cadena)) # 10

# Se pueden multiplicar cadenas
print(cadena * 2) # Hola MundoHola Mundo

# Concatenacion
print(cadena + " " + name3) # Hola Mundo Pedro


# Subcadenas
print(cadena[0:4]) # Hola
print(cadena[5:10]) # Mundo

# Cadenas y sus funciones
print(cadena.upper()) # HOLA MUNDO
pivot = cadena.strip()
print(pivot) # HOLA MUNDO
