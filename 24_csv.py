import csv
from typing import Sequence

# Leer un archivo
"""with open("./seed/products.csv", mode="r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)"""


# Mostar la informacion por columnas
"""with open("./seed/products.csv", mode="r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Producto: {row['name']}, Precio: {row['price']}")
"""

# Agregar informacion al archivo
"""
new_product = {
    "name": "Test Product",
    "price": "100.00",
    "quantity": "10",
    "brand": "Test",
    "category": "Accessories",
    "entry_date": "2023-01-01",
}

with open("./seed/products.csv", mode="a", newline="") as file:
    csv_writer = csv.DictWriter(
        file,
        fieldnames=new_product.keys(),
    )
    csv_writer.writerow(new_product)"""

# Creando un archivo desde otro pero actualizado
#
file_path = "./seed/products.csv"

update_file_path = "./seed/products_updated.csv"

with open(file_path, mode="r") as file:
    csv_reader = csv.DictReader(file)
    fieldnames = csv_reader.fieldnames or []
    fieldnames = list(fieldnames) + ["total_value"]
    with open(update_file_path, mode="w", newline="") as ufile:
        csv_writer = csv.DictWriter(
            ufile,
            fieldnames=fieldnames,
        )
        csv_writer.writeheader()  # Escribir encabezado
        for row in csv_reader:
            row["total_value"] = float(row["price"]) * int(row["quantity"])
            csv_writer.writerow(row)
