for i in range(100, 111):
  print("Day ", i)
print()
print("Thirteen Times Table")
for i in range(1, 13):
  print(i, "x 13 =", i * 13)
print()
#for i in range(0, 1000000, 25):
#  print(i)
print()
for i in range(10, -1, -1):
  print(i)
print()
print()
print("List Generator")
print()
print("Welcome to your list generator. I will ask you for a starting number, ending number, and increment to use.")
print()

x = int(input("What number do you want to start with? "))
y = int(input("What number do you want to end with? "))
z = int(input("How many should I add each time? "))

for i in range(x, y, z):
  print(i)
