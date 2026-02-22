import random

best_score = None  # To track minimum attempts

while True:
    number = random.randint(1, 100)
    attempts_left = 7
    attempts_used = 0

    print("\n=== NUMBER GUESSING GAME ===")
    print("Guess a number between 1 and 100")
    print("You have 7 attempts!")

    while attempts_left > 0:
        guess = int(input("Enter your guess: "))
        attempts_used += 1
        attempts_left -= 1

        if guess == number:
            print("Congratulations! You guessed it correctly.")
            print("Attempts used:", attempts_used)

            # Update best score
            if best_score is None or attempts_used < best_score:
                best_score = attempts_used
                print(" New Best Score:", best_score, "attempt(s)")

            break

        elif guess > number:
            print("Too High!")
        else:
            print("Too Low!")

        # Bonus Hint (within 5)
        if abs(guess - number) <= 5 and guess != number:
            print(" Very Close!")

        print("Attempts remaining:", attempts_left)

    else:
        print("Game Over! The number was:", number)

    # Play again option
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break