import json
from typing import TypedDict


# Definición del tipo para un producto
class Product(TypedDict):
    name: str
    price: int
    quantity: int
    brand: str
    category: str
    entry_date: str


file_path = "seed/products.json"

new_product: Product = {
    "name": "New Product",
    "price": 100,
    "quantity": 10,
    "brand": "Brand",
    "category": "Category",
    "entry_date": "2023-01-01",
}


# Lectura del archivo JSON
with open(file_path, "r") as file:
    products: list[Product] = list[Product](json.load(file))

# Mostrar el contenido de los productos
for product in products:
    print(product)


# Agregar el nuevo producto a la lista de productos
products.append(new_product)

# Escribir los productos actualizados en el archivo JSON
with open(file_path, "w") as file:
    json.dump(products, file, indent=2)
