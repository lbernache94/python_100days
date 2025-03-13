#for counter in range(1,11):
#  print(counter)

loan = 1000
apr = 0.05
for years in range(10):
  loan += (loan*apr)
  print("Year", years+1, "is", round(loan,2))
  print()
print("You have paid", round(loan-1000,2), "in interest")