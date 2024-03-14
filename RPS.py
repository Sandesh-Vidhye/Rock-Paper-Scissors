# Sandesh Vidhye 
import random

def play_rock_paper_scissors():
  """Plays a round of Rock-Paper-Scissors against the computer."""

  options = ["Rock", "Paper", "Scissors"]
  
  user_choice = input("Enter your choice (Rock, Paper, Scissors): ").upper()

  if user_choice not in options:
    print("Invalid choice. Please try again.")
    return

  computer_choice = random.choice(options)

  if user_choice == computer_choice:
    print("It's a tie!")
  elif (user_choice == "Rock" and computer_choice == "Scissors") or \
       (user_choice == "Paper" and computer_choice == "Rock") or \
       (user_choice == "Scissors" and computer_choice == "Paper"):
    print("You win!")
  else:
    print("You lose!")

  print(f"Computer chose: {computer_choice}")

play_rock_paper_scissors()
