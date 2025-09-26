x = 5
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
print("This is the end of the if-elif-else statement")


x = 15
y = 20

if x > 10 and y > 25:  # operador AND para comparar dos condiciones
    print("x is greater than 10 and y is greater than 25")

if x > 10 or y > 25:  # operador OR para comparar dos condiciones
    print("x is greater than 10 or y is greater than 25")

if not x > 10:  # Negacion de if
    print("x is not greater than 10")

# If anidados
is_member = True
age = 25
if is_member:
    if age >= 18:
        print("Welcome, member!")
    else:
        print("Welcome, member, but you are underage.")
else:
    print("Welcome, guest!")


# Juego de Piedra, Papel o Tijera
import random

options = ["rock", "paper", "scissors"]
player_choice = input("Choose rock, paper, or scissors: ").lower()
cpu_choice = random.choice(options)

print("CPU choice was:", cpu_choice)
print("Player choice was:", player_choice)

if player_choice == cpu_choice:
    print("It's a tie!")
elif player_choice == "rock" and cpu_choice == "scissors":
    print("You win!")
elif player_choice == "paper" and cpu_choice == "rock":
    print("You win!")
elif player_choice == "scissors" and cpu_choice == "paper":
    print("You win!")
else:
    print("You lose!")
