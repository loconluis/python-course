from multiprocessing import Value
from string import printable


to_do = ["Go to the hotel", "Go to lunch", "Visit a museum", "Go back to the hotel"]
print(to_do)
print(type(to_do))  # Clase List

numbers = [1, 2, 3, 4, 5, "Cinco"]
print(numbers)
print(type(numbers))  # Clase List

mix = [1, "dos", 3.0, True]
print(mix)
print(len(mix))  # Longitud de la lista mix
print(type(mix))  # Clase List

# Indexacion
print(mix[0])  # Primer elemento de la lista mix
print(mix[1])  # Segundo elemento de la lista mix
print(mix[2])  # Tercer elemento de la lista mix
print(mix[3])  # Cuarto elemento de la lista mix

print(mix[0:2])  # Primeros dos elementos de la lista mix
print(mix[:3])  # Primeros tres elementos de la lista mix
print(mix[2:])  # desde el element 2 hasta el final de la lista mix

# Aumentar un valor a la lista mix
mix.append("cuatro")
print(mix)

mix.insert(2, ["a", "b"])  # @ignore
print(mix)

values = [1, 2, 3, 100, 98, 76, 4, 5, 6]
print(values)
print("Mayor que:", max(values))
print("Menor que:", min(values))
print("Suma:", sum(values))
print("Promedio:", sum(values) / len(values))
