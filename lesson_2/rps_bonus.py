import random

VALID_CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]

def prompt(message):
    print(f"==> {message}")

def display_choice(player, computer):
    prompt(f"You chose {player}, computer chose {computer}")

def determine_winner(player, computer):
    if ((player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper") or
        (player == "spock" and computer == "rock") or
        (player == "lizard" and computer == "spock")
        ):
        return 'player'
    elif ((player == "rock" and computer == "paper") or
          (player == "paper" and computer == "scissors") or
          (player == "scissors" and computer == "rock") or
          (player == "spock" and computer == "lizard") or
          (player == "lizard" and computer == "rock")
          ):
        return 'computer'
    else:
        return 'tie'

def display_winner(winner):
    match winner:
        case 'player':
            prompt("You win!")
        case 'computer':
            prompt("Computer wins.")
        case _:
            prompt("It's a tie.")

while True:

    player_score = 0
    computer_score = 0
    plays = 0

    while plays < 5:

        prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
        choice = input()

        while choice not in VALID_CHOICES:
            prompt("That's not a valid choice")
            choice = input()

        computer_choice = random.choice(VALID_CHOICES)

        display_choice(choice, computer_choice)
        winner = determine_winner(choice, computer_choice)
        display_winner(winner)
        
        plays += 1
        if winner == 'player':
            player_score += 1 
        elif winner == 'computer': 
            computer_score += 1

        print(plays)

    prompt(f"You won {player_score} times. Computer won {computer_score} times.")

    prompt("Do you want to play again (y/n)?")
    answer = input().lower()
    while answer == '' or (answer[0] != 'n' and answer[0] != 'y'):
        prompt('Please enter "y" or "n".')
        answer = input().lower()

    if answer[0] != "y":
        break