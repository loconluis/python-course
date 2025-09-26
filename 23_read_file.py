# Leer un archivo linea por linea
"""with open("./seed/story.txt", "r") as file:
for line in file:
    print(line.strip())"""

# Leer todas las lineas en una lista
with open("./seed/story.txt", "r") as file:
    lines = file.readlines()
    print(lines)


with open("./seed/story.txt", "a") as file:
    file.write("\n\nBy: Ai Writer\n")

# with open("./seed/story.txt", "w") as file:
#     file.write("\n\nBy: Ai Writer\n")  Sobreeescribe todo un archivo
