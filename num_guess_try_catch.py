# !/user/bin/env python3

# Created by Kevin Csiffary
# Date: Oct. 17, 2022
# This program gets the user to guess a randomly selected number
# it also has error checking

# imports required libraries
import random


def main():
    # generates random number
    random_int = random.randint(0, 9)

    # asks user for their guess
    print("I'm thinking of a number between 0 and 9")
    user_guess = input("What is your guess? ")

    # adds extra line
    print("")

    # tries to cast the users guess into an integer
    try:
        user_guess = int(user_guess)

    # if it cannot cast, display that the input is invalid
    except:
        print(f"{user_guess} is an invalid integer")

    # if it succeeds
    else:
        # check if the guess is correct or incorrect
        if user_guess == random_int:
            print("You guessed correctly!")
        else:
            print(f"You guessed incorrectly, the correct answer was {random_int}")

    # regardless of the result, thank the user for playing
    finally:
        print("\nThank you for playing!")


if __name__ == "__main__":
    main()
