import random

def get_choice():
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    try:
        if player_choice not in ["rock", "paper", "scissors"]:
            raise ValueError("Invalid choice")
    except ValueError as e:
        print(e)
        return get_choice()
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices={"player": player_choice, "computer": computer_choice}
    return choices
def get_win(player,computer):
    player = choices["player"]
    computer = choices["computer"]
    print(f"player choices: {player} computer choices: {computer}")
    if player == computer:
        return "Its a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "You win! Rock crushes scissors."
        else:
            return "You lose! Paper covers rock."
    elif player == "paper":
        if computer == "rock":
            return "You win! Paper covers rock."
        else:
            return "You lose! Scissors cuts paper."
    elif player == "scissors": 
        if computer == "paper":
            return "You win! Scissors cuts paper."
        else:
            return "You lose! Rock crushes scissors."
    
choices=get_choice()
result=get_win(choices["player"], choices["computer"])
print(result)
