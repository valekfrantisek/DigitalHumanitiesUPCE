# This is a sample Python script.
from random import randint

import random

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def startGame(min, max, attemtps):
    print(f"Guess the number  {min} - {max}, attempts: {attemtps}")
    guessed_number = random.randint(min, max)
    # NOTE: když jste importovala "from random import randint", tak tohle je zbytečné, stačilo napsat jenom guessed_number = randint(min, max)

    while attemtps != 0:
        user_input = input("Type number: ")  # Read string from console
        try:
            number = int(user_input)  # Convert string to number
            if number > guessed_number:
                print(f"{number}: Your number is greater!")
            elif number < guessed_number:
                print(f"{number}: Your number is less")
            elif number == guessed_number:
                print(f"You win! Number was: {number}")
                break
            attemtps = attemtps - 1
            print(f"attempts: {attemtps}")

        except Exception as e:
            print(f"{e}")

def main():
    print("Hello world")
    startGame(0,100,10)


if __name__ == "__main__":
    main()