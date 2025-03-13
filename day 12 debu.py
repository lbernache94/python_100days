print("100 Days of Code QUIZ")
print()
print("How many can you answer correctly?")
ans1 = str(input("What language are we writing in?: "))
if ans1 == "python":
  print("Correct")
else:
  print("Nope🙈")
ans2 = int(input("Which lesson number is this?: "))
if ans2 == 12:
  print("That's right!😎")
elif ans2 != 12:
  print("We're not quite that far yet")
else:
  print("That's not a number")