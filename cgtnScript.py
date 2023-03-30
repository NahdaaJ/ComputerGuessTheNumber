# COMPUTER GUESS THE NUMBER
# Author: Nahdaa Jawed
# Date Started: 30/03/2023 15:38
# Date Finished: -
# Description: -

import random

def guessNum():
    goLow = 100
    goHigh = 1
    userFeedback = ''
    countGuess = 0
    playAgain = 0

    while playAgain != "N":

        while userFeedback!= "Y":
            if goLow != goHigh:
                compGuess = random.randint(goHigh, goLow)
            else:
                compGuess = goLow

            userFeedback = input(f'\nIs {compGuess} your number?\nGo Higher (H), Go Lower (L), Yes (Y) ')
            if userFeedback == "H":
                goHigh = compGuess+1

            elif userFeedback == "L":
                goLow = compGuess - 1

            countGuess = countGuess + 1

        print(f'\nThe computer has guessed the number {compGuess} correctly!'
            f'\nIt took the computer {countGuess} guesses!')

        playAgain = input("\nWould you like to play again? (Y/N)\n")
        if playAgain == "Y":
            goLow = 100
            goHigh = 1
            userFeedback = ''
            countGuess = 0

    print("\nThanks for playing!")

guessNum()