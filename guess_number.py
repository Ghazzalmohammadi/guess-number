import random

# Show a welcome message when the game starts
print("Welcome to the Number Guessing Game!")
print("I picked a number between 1 and 20.")
print("Let's see if you can guess it.")

# Choose a random number between 1 and 20
secret_number = random.randint(1, 20)

# Start counting the attempts from zero
attempts = 0

# Keep the game running until the correct number is guessed
while True:

    # Ask the user to enter a guess
    guess = int(input("Enter your guess: "))

    # Add one to the number of attempts
    attempts += 1

    # Check if the guess is smaller than the secret number
    if guess < secret_number:
        print("Wrong! My number is higher.")

    # Check if the guess is bigger than the secret number
    elif guess > secret_number:
        print("Wrong! My number is lower.")

    # If neither condition is true, the guess is correct
    else:
        print("Congratulations! You guessed the correct number.")
        print(f"Number of attempts: {attempts}")

        # The correct number was guessed, so we leave the loop
        break
