#counter = 0
#while counter < 100:
#print(counter)
#counter += 10

#########################

#exit = ""
#while exit != "yes":
  #print("🥳")
  #exit = input("Exit?: ")

#########################

animal = ""
while animal != "cow":
  print("Let's Play.")
  print()
  animal = input("What animal do you want?: ")
  if animal == "dog":
    print("A dog goes woof.")
  elif animal == "cat":
    print("A cat goes meow.")
  elif animal == "bird":
    print("A bird goes tweet.")
  elif animal == "pig":
    print("A pig goes oink.")
  else:
    print("I don't know that animal.")
exit = ""

while exit != "Yes" and exit != "yes":
  print("Ok")
  print()
  exit = input("Do you really want to exit?: ")
animal = ""


while animal != "Rat" or animal != "rat":
  print("A rat goes squeak.")
  animal = input("What animal do you want?: ")
  if animal == "Snake" or animal == "snake":
    print("A snake goes hiss.")
  elif animal == "Frog" or animal == "frog":
    print("A frog goes ribbit.")
  elif animal == "Duck" or animal == "duck":
    print("A duck goes quack.")
  else:
    print("I cannot imitate that animal.")
  break