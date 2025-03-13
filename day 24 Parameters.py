import random

print("Infinity Dice 🎲")

sides = int(input("How many sides?: "))
playGame = "yes"

def rolDice(sides):
  print("You rolled ", random.randint(1,sides))
while playGame == "yes":
  rolDice(sides)
  playGame = input("Roll again?")
  print()