import statistics

import csv

monthly_sales = {}

with open("seed/sales_yearly.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row["month"]
        sales = float(row["sales"])
        monthly_sales[month] = sales


sales = list(monthly_sales.values())


print(sales)

# Hallar la media de las ventas
mean_sales: float = statistics.mean(sales)
print(f"La media de las ventas es: {mean_sales:.2f}")

# Hallar la moda de las ventas
mode_sales = statistics.mode(sales)
print(f"La moda de las ventas es: {mode_sales:.2f}")

# Hallar la mediana de las ventas
median_sales = statistics.median(sales)
print(f"La mediana de las ventas es: {median_sales:.2f}")

# Hallar la desviación estándar de las ventas
std_dev_sales = statistics.stdev(sales)
print(f"La desviación estándar de las ventas es: {std_dev_sales:.2f}")

# Hallar la varianza de las ventas
variance_sales = statistics.variance(sales)
print(f"La varianza de las ventas es: {variance_sales:.2f}")
