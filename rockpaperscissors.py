import random


# Function to get user input with input validation
def get_user_input():
    while True:
        user_choice = input("What is your choice [rock, paper, scissor]: ").lower()
        if user_choice not in possible_outcomes:
            print("Invalid Input!!")
        else:
            print("Processing...")
            return user_choice


# Function to determine the winner of the game
def determine_winner(user_choice, computer_choice):
    print(f"\nUser's Choice: {user_choice.capitalize()} \nComputer's Choice: {computer_choice.capitalize()}\n")

    global user_wins, computer_wins, draws
    if user_choice == computer_choice:
        print("It's a draw, both have the same choices.")
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


# Function to ask if the user wants to play again
def play_again():
    return input("Do you want to play again? [y] for YES and [n] for NO: ").lower() == "y"


# List of possible outcomes for the game
possible_outcomes = ["rock", "paper", "scissor"]

# Initial scores
user_wins = 0
computer_wins = 0
draws = 0

# Main game loop
while True:
    # Get user input and generate computer choice
    user_choice = get_user_input()
    computer_choice = random.choice(possible_outcomes)

    # Determine the winner and update scores
    determine_winner(user_choice, computer_choice)

    # Ask if the user wants to play again
    if play_again():
        print("Let's play again.")
    else:
        print("Thanks for playing.")
        break

# Display final scores
print(f"USER'S SCORE: {user_wins}, COMPUTER'S SCORE: {computer_wins}, DRAW: {draws}")
