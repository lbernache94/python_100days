def get_player_choice(player):
  choice = input(f"Player {player}, enter your choice (R for Rock, P for Paper, S for Scissors): ").upper()
  while choice not in ["R", "P", "S"]:
      choice = input(f"Invalid choice. Player {player}, please enter R, P, or S: ").upper()
  return choice

def determine_winner(player1_choice, player2_choice):
  if player1_choice == player2_choice:
      return "It's a tie! 🤝"

  if (player1_choice == "R" and player2_choice == "S") or \
     (player1_choice == "S" and player2_choice == "P") or \
     (player1_choice == "P" and player2_choice == "R"):
      return "Player 1 wins! 🎉"

  return "Player 2 wins! 🎉"

def play_game():
  print("Welcome to the Rock, Paper, Scissors Battle! ⚔️")
  while True:
      player1_choice = get_player_choice(1)
      player2_choice = get_player_choice(2)

      choices = {"R": "Rock 🪨", "P": "Paper 📄", "S": "Scissors ✂️"}

      print(f"\nPlayer 1 chose: {choices[player1_choice]}")
      print(f"Player 2 chose: {choices[player2_choice]}")

      print(determine_winner(player1_choice, player2_choice))

      play_again = input("\nDo you want to play again? (yes/no): ").lower()
      if play_again != 'yes':
          break

  print("Thanks for playing! 🎮")

# Run the game
play_game()