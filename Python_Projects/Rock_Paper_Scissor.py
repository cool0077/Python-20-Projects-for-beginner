import random

def get_choices():
  player_choice = input("enter (rock, paper or scissor): ")
  options = ["rock","paper","scissor"]
  computer_choice = random.choice(options)
  choices={"player":player_choice, "computer":computer_choice}
  return choices
  
def check_win(player,computer):
  print(f"You chose {player} ,and computer chose {computer}")

  if player == computer:
    return "It's a tie."
  elif player == "rock":
    if computer == "scissor":
      return "Rock smashes Scissor You win!!"
    else:
      return "Paper convers Rock You Lose."

  elif player == "paper":
    if computer == "rock":
      return "Paper cover Rock You Win!!"
    else:
      return "Scissor cuts Paper You Lose."

  elif player == "scissor":
    if computer == "paper":
      return "Scissor cuts Paper You Win!!"
    else:
      return "Rock smashes Scissor You Lose."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)