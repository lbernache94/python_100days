def login():
  while True:
    username = input("Insert your username: ")
    password = input("Insert your password: ")
    if username == "username" and password == "password":
      print("Welcome to replit! ")
      break
    else:
      print("Whoops! I don't recognize that username or password. Try again! ")
      continue

print("Replit Login System")
login()