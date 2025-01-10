# Eva Deng
# P1. 11/11/24
# Random Guessing Game

from random import randint

def generator(range_end):
    #Generates a random number within the specified range.
    return randint(1, range_end)

def guessing_game():
    #A guessing game where the user has to guess a random number within a given range in three attempts.

    print("Welcome to the Guessing Number Game!")
    print("Choose your difficulty level:")
    print("1. Easy (1-10)")
    print("2. Medium (1-20)")
    print("3. Hard (1-30)")

    # Get the difficulty level
    difficulty = int(input("Enter your choice (1, 2, or 3): "))
    if difficulty == 1:
        range_end = 10
    elif difficulty == 2:
        range_end = 20
    elif difficulty == 3:
        range_end = 30
    else:
        print("Invalid choice! Defaulting to Easy level.")
        range_end = 10

    random_number = generator(range_end)
    guess_left = 3

    while guess_left > 0:
        try:
            guess = int(input(f"Guess a number between 1 and {range_end}: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if guess == random_number:
            print("Congrats! You guessed the correct number!")
            break
        elif guess < random_number:
            print("Too low!")
        else:
            print("Too high!")

        guess_left -= 1
        print(f"You have {guess_left} {'guess' if guess_left == 1 else 'guesses'} left.")

    if guess_left == 0:
        print(f"Sorry, you lost. The correct number was {random_number}.")

def main():
    #Main function to run the game and offer replay options.
    while True:
        guessing_game()
        play_again = input("Would you like to play again? (yes or no): ").strip().lower()
        if play_again != "yes":
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
