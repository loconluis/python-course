numbers = {1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco"}

print(numbers)
print(type(numbers))
print(numbers[3])
print(numbers[5])

info = {"name": "John", "age": 30, "city": "New York", "email": "john@example.com"}
del info["email"]
print(info)

claves = info.keys()
print(claves)
print(type(claves))
_values = info.values()
print(_values)
print(type(_values))
items = info.items()
print(items)
print(type(items))

# Agenda de contactos
info2 = {
    "John": {
        "name": "John",
        "age": 30,
        "city": "New York",
        "email": "john@example.com",
    },
    "Jane": {
        "name": "Jane",
        "age": 25,
        "city": "Los Angeles",
        "email": "jane@example.com",
    },
}
print(info2)
print(info2["John"])
print(info2["Jane"])
