#while True:
#  print("Tris program will forever runing")
#  goAgain = input("You want to go again?: ")
#  if goAgain == "no":
#    break
#print("Aww, I was having a good time!")


#counter = 0
#while True:
#  answer = int(input("Enter a number: "))
#  print("Adding it up!")
#  counter += answer
#  print("Current total is", counter)
#  addAnother = input("Add another? ")
#  if addAnother == "no":
#    break
#print("Bye!")

counter = 0
while True:
  print("Fill in the blank lyrics!")
  print("Type in the blank lyrics and see if you are as cool as me")
  print("Ella es ______ para sex es atrevida")
  lyric = input("What is the missing lyric?: ")
  if lyric == "calladita":
    print("Well done! It only took you", counter, "attempts.")
    break
  counter += 1
print("Nope, try again.")