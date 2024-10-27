import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play, or 'quit' to exit.\n")

    # Define possible moves
    moves = ["rock", "paper", "scissors"]

    while True:
        # Get user move
        user_move = input("Your move: ").lower()

        # Check if user wants to quit
        if user_move == "quit":
            print("Thanks for playing! Goodbye!")
            break

        # Check if user move is valid
        if user_move not in moves:
            print("Invalid move! Please try again.\n")
            continue

        # Generate computer move
        computer_move = random.choice(moves)
        print(f"Computer chose: {computer_move}")

        # Determine the outcome
        if user_move == computer_move:
            print("It's a tie!\n")
        elif (user_move == "rock" and computer_move == "scissors") or \
             (user_move == "paper" and computer_move == "rock") or \
             (user_move == "scissors" and computer_move == "paper"):
            print("You win!\n")
        else:
            print("You lose!\n")

# Start the game
rock_paper_scissors()