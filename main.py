import math
from random import *


def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)


def ComputerGuess():
    print("Pick a number between 1-100")
    Lowest = 0
    Highest = 100
    GuessCounter = 7
    while True:

        Middle = Lowest + normal_round((Highest - Lowest) / 2)

        print("My guess is:", Middle)

        Option = input(
            "Enter 1 if it is correct. Enter 2 if my guess is higher than your number. Enter 3 if my guess is lower than your number: ")

        if Option == "1":
            print("I won")
            break
        if Option == "2":
            Highest = Middle
        if Option == "3":
            Lowest = Middle
        GuessCounter -= 1
        print("Guesses remaining:", GuessCounter)
    print("It took me:", 7 - GuessCounter, "guesses")


# End of ComputerGuess
# Start of PlayerGUess
def PlayerGuess():
    print("I have chosen a number between 1 and 100, you have 7 tries to guess that number: ")
    ComputerChoice = randint(1, 100)

    Lowest = 1
    Highest = 100
    GuessCount = 7
    for i in range(7):

        Guess = int(input("Enter your guess: "))
        GuessCount -= 1
        if Guess == ComputerChoice:
            print("Your guess is correct, you win!")
            break
        if Guess != ComputerChoice:
            print("Your guess is incorrect, try again")
            if Guess > ComputerChoice:
                Highest = Guess
            else:
                Lowest = Guess
        print("Your new guess range is between: " + str(Lowest) + " and " + str(Highest))
        print("Guesses remaining: ", GuessCount)
    print("You have run out of guesses, my actual number was: ", ComputerChoice)


Menu = input("For the computer to guess your number enter 1, For you to guess the computer number enter 2: ")
if Menu == "1":
    ComputerGuess()
if Menu == "2":
    PlayerGuess()