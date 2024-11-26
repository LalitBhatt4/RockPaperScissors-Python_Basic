import random

def get_choices():
    options = ["Rock", "Paper", "Scissors"]
    user_choice= input("Enter your move (rock, paper, scissors): ")
    computer_choice= random.choice(options)

    choices= {"player": user_choice, "computer": computer_choice}

    return choices


def winner(player, computer):
    print(f"You chose {player}, computer chose {computer}")

    if player == computer:
        return "  It's a tie!"
    elif player=="rock" and computer=="scissors":
        return "  You win!"
    elif player=="paper" and computer=="rock":
        return "  You win!"
    elif player=="scissors" and computer=="paper":
        return "  You win!"
    else: return "  You lose..."
    
choices= get_choices()
result = winner(choices["player"], choices["computer"])

print(result)