print("Grade Generator")
print()
NameOfTest = input("What's your test name? ")
print()
MaxScore = int(input("What's the maximum score you can get? "))
print()
YourScore = int(input("What's your score? "))
if YourScore >= 90 and YourScore <= 100:
  print("You got" , YourScore ,"in your", NameOfTest, "which is an A+")
elif YourScore >= 80 and YourScore <= 89:
  print("You got" , YourScore ,"in your", NameOfTest, "which is an A-")
elif YourScore >= 70 and YourScore <= 79:
  print("You got" , YourScore ,"in your", NameOfTest, "which is a B")
elif YourScore >= 60 and YourScore <= 69:
  print("You got" , YourScore ,"in your", NameOfTest, "which is a C")
elif YourScore >= 50 and YourScore <= 59:
  print("You got", YourScore,"in your", NameOfTest, "which is a D")
elif YourScore <= 50:
  print("You got", YourScore,"in your", NameOfTest, "which is a U")
else:
  print("Try again!")

  #######################################################################

print("Grade Generator")
print()
testName = input("What is the name of the test? ")
maxScore = int(input("What is the maximum score you could receive? "))
yourScore = int(input("What is the score you received? "))
print()
numberScore = float(yourScore / maxScore)
finalNumber = round(numberScore, 2)
finalPercentage = round(float(yourScore / maxScore)*100, 2)
print("You got",finalPercentage,"%")
if finalNumber >= .90:
  print("Your letter score is an A+")
elif finalNumber >= .80 and finalNumber <= .89:
  print("Your letter grade is an A-.")
elif finalNumber >= .70 and finalNumber <= .79:
  print("Your letter score is a B.")
elif finalNumber >= .60 and finalNumber <= .69:
  print("Your letter grade is a C.")
elif finalNumber >= .50 and finalNumber <= .59:
  print("Your letter grade is a D.")
elif finalNumber <= .49:
  print("Your letter grade is a U.")
else:
  print("Try again!")