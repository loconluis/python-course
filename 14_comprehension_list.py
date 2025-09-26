# Una Comprehension List es una forma concisa de crear listas en Python,
# pues permite generar listas nuevas transformando cada elemento de una colección existente
# o creando elementos a partir de un rango. La sintaxis es compacta y directa,
# lo que facilita la comprensión del propósito de tu código de un vistazo.
# [expresión for elemento in iterable if condición]

squares = [x**2 for x in range(1, 11)]
print("Cuadradoss: ", squares)

# Celsius to Fahrenheit
celsius_temps = [0, 10, 20, 30, 40]
fahrenheit_temps = [temp * 9 / 5 + 32 for temp in celsius_temps]
print("Temperaturas en Fahrenheit: ", fahrenheit_temps)

# Fahrenheit to Celsius
fahrenheit_temps = [32, 68, 100, 130, 160]
celsius_temps = [(temp - 32) * 5 / 9 for temp in fahrenheit_temps]
print("Temperaturas en Celsius: ", celsius_temps)

# Numeros Pares
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print("Numeros Pares: ", even_numbers)

# Matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)
