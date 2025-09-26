my_list = [1, 2, 3, 4, 5, 6]

my_iter = iter(my_list)

# Vamos a usar el iterador
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# Crear un iterador para los numeros impares

# Limite
limit = 10

# Crear iterador
odd_itter = iter(range(1, limit + 1, 2))

# Usar el iterador
for num in odd_itter:
    print(num)

# Iterar en cadenas
# Creando la cadena
text = "Hola mundo"
# Creando el iterador
iter_text = iter(text)

# Iterar en la cadena
for char in iter_text:
    print(char)


# Fibonacci
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


for num in fibonacci(20):
    print(num)
