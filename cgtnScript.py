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

    while userFeedback!= "Y":
        if goLow != goHigh:
            compGuess = random.randint(goHigh, goLow)
        else:
            compGuess = goLow

        userFeedback = input(f'\nIs {compGuess} your number?\nHigher (H), Lower (L), Yes (Y) ')
        if userFeedback == "H":
            goHigh = compGuess+1

        elif userFeedback == "L":
            goLow = compGuess - 1

        countGuess = countGuess + 1

    print(f'\nThe computer has guessed the number {compGuess} correctly!'
          f'\nIt took the computer {countGuess} guesses!')


guessNum()