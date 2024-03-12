import random
def get_choices():
    player_choice = input("Enter a choice (rock (r), paper (p), scissors (s): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices
def check_win(player, computer):
    print("You chose " + player + ", computer chose: " + computer)
    print(f"You chose {player}, Computer chose {computer}")
    if player == computer:
        return "Its a tie"
    elif player == "rock":
        if computer == "scissors":
            return "rock smashes scissors you win!"
        else:
            return "paper covers rock you lose"
    elif player == "paper":
        if computer == "rock":
            return "paper covers rock you win!"
        else:
            return "Scissor cuts paper you lose"
    elif player == "scissor":
        if computer == "paper":
            return "scissor cuts paper you win!"
        else:
            return "rock smashes scissors you lose"
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
