print("How many seconds are in a year?")
print()
print("Let's find out!")
print()
print("There are 60 seconds in a minute.")
print("There are 60 minutes in an hour.")
print("There are 24 hours in a day.")
print("There are 365 days in a year.")
print()
print("Some years are leap years, which means there are 366 days instead of 365.")
Normal_Year = str(input("Is it a normal year? "))
if Normal_Year == "Yes" or Normal_Year == "Yes":
  print("This year has", 60*60*24*365, "seconds.")
elif Normal_Year == "No":
  print("Then this year is a leap year so has", 60*60*24*366, "seconds.")
else:
  print("Please answer with Yes or No.")
