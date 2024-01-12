import random

def get_user_input():
    while True:
        user_choice = input("What is your choice [rock, paper, scissor]: ").lower()
        if user_choice not in possible_outcomes:
            print("Invalid Input!!")
        else:
            print("Processing...")
            return user_choice
        
def determine_winner(user_choice, computer_choice):
    print(f"\nUser's Choice: {user_choice.capitalize()} \nComputer's Choice: {computer_choice.capitalize()}\n")

    global user_wins, computer_wins, draws
    if user_choice == computer_choice:
        print("It's a draw, both have same choices.")
        draws += 1
    elif (
        (user_choice == "rock" and computer_choice == "scissor") or
        (user_choice == "scissor" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("THE USER HAS WON THE GAME.")
        user_wins += 1 
    else:
        print("THE COMPUTER HAS WON THE GAME.")
        computer_wins += 1

def play_again():
    return input("Do you want to play again? [y] for YES and [n] for NO: ").lower() == "y"

possible_outcomes = ["rock", "paper", "scissor"]
user_wins = 0
computer_wins = 0
draws = 0

while True:
    user_choice = get_user_input()
    computer_choice = random.choice(possible_outcomes)
    determine_winner(user_choice, computer_choice)

    if play_again():
        print("Let's play again.")
    else:
        print("Thanks for playing.")
        break
    
print(f"User's Score: {user_wins}, Computer's Score: {computer_wins}, Draw: {draws}")