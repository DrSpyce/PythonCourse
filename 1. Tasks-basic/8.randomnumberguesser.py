import random

secret_number = random.randint(1, 100)

while True:
    try:
        user_guess = int(input("Guess the number (between 1 and 100): "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    if user_guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif user_guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")