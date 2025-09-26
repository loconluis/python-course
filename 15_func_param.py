# Vamos a crear una calculadora basica con funciones


def suma(a: int, b: int) -> int:
    return a + b


def resta(a: int, b: int) -> int:
    return a - b


def multiplicacion(a: int, b: int) -> int:
    return a * b


def division(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b


print("Hola bienvenido a la calculadora")
print("Seleccione una operacion:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")

opcion = int(input("Ingrese la opcion deseada: "))

if opcion == 1:
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    print("El resultado es:", suma(a, b))
elif opcion == 2:
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    print("El resultado es:", resta(a, b))
elif opcion == 3:
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    print("El resultado es:", multiplicacion(a, b))
elif opcion == 4:
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    print("El resultado es:", division(a, b))
else:
    print("Opcion invalida")
