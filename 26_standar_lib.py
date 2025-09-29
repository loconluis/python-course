import os

cwd = os.getcwd()
print("Current working directory:", cwd)


# Listar los archivos .txt
txt_files = [f for f in os.listdir("./seed") if f.endswith(".txt")]
print("Text files:", txt_files)


"""os.rename("./seed/story.txt", "./seed/story_renamed.txt")
print("File renamed successfully.")"""


# Cosas con Math
import math
# Hallar el area y perimetro de un circulo

radius = 5
area = math.pi * radius**2
perimeter = 2 * math.pi * radius
print("Area:", area)
print("Perimeter:", perimeter)


# Random con la libreria random

import random

random_number = random.randint(1, 100)
print("Random number:", random_number)

# random colors selection
color = random.choice(["red", "green", "blue"])
print("Random color:", color)


# Barajear una lista de cartas
cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
random.shuffle(cards)
print("Shuffled cards:", cards)
