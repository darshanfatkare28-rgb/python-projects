import random

# Store player scores
player_score = 0
computer_score = 0

# Available options
choices = ["stone", "paper", "scissor"]

print("===== STONE PAPER SCISSORS GAME =====")
print("First to score more points wins!")
print("Type 'exit' to stop the game.")

while True:

    # Computer selects a random option
    computer = random.choice(choices)

    # Get player's choice
    player = input(
        "\nChoose stone, paper, scissor or exit: "
    ).strip().lower()

    # Stop the game
    if player == "exit":
        print("\nThanks for playing!")
        break

    # Check whether the choice is valid
    if player not in choices:
        print("Wrong input! Please try again.")
        continue

    print(f"Your choice: {player}")
    print(f"Computer choice: {computer}")

    # Decide the winner
    if player == computer:
        print("It's a tie!")

    elif (
        (player == "stone" and computer == "scissor")
        or (player == "paper" and computer == "stone")
        or (player == "scissor" and computer == "paper")
    ):
        player_score += 1
        print("You won this round!")

    else:
        computer_score += 1
        print("Computer won this round!")

    # Show updated scores
    print("\n----- CURRENT SCORE -----")
    print(f"Player: {player_score}")
    print(f"Computer: {computer_score}")

# Show the final result
print("\n===== FINAL RESULT =====")
print(f"Your Total Score: {player_score}")
print(f"Computer Total Score: {computer_score}")

if player_score > computer_score:
    print("Congratulations! You are the winner!")

elif computer_score > player_score:
    print("Better luck next time! Computer wins!")

else:
    print("Great game! The final score is a tie.")

print("Game ended successfully!")