import random

def guess_the_number():
    """
    This function implements the 'Guess the Number' game.
    The computer picks a random number between 1 and 100,
    and the player has to guess it.
    """
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    print("I'm thinking of a number between 1 and 100.")

    # Initialize the number of guesses
    attempts = 0

    while True:
        try:
            # Prompt the user for their guess
            guess = int(input("What's your guess? "))
            attempts += 1

            # Compare the guess with the secret number
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break  # Exit the loop if the guess is correct
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    guess_the_number()