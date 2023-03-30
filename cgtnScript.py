# COMPUTER: GUESS THE NUMBER
# Author: Nahdaa Jawed
# Date Started: 30/03/2023 15:38
# Date Finished: 30/03/2023 23:14
# Description:  A game where the user is prompted to choose a number between 1 and 100.
#               The program then guesses the users number, and the user can provide feedback such as higher or lower.
#               When the program guesses the number correctly, the user can tell the program.
#               The program then prints a happy message and the amount of guesses it took.
#               Then the program asks if the user wants to play again, choosing Y loops through the game again,
#               choosing N ends the program.

# Importing relevant modules and functions.
import random

# Defining the game as a function.
def guessNum():

    # Initialising variables.
    goLow = 100 # We
    goHigh = 1
    userFeedback = ''
    countGuess = 0
    playAgain = 0

    # If the user wants to play again, the program loops back to the beginning.
    while playAgain != "n":
        print("\nPick a number between 1 and 100 inclusive.")

        # While the programs guess is incorrect:
        while userFeedback != "y":
            if goLow != goHigh:
                compGuess = random.randint(goHigh, goLow) # Generates a random integer in the bounds where we know the answer is correct.
            else:
                compGuess = goLow

            # Asking user for feedback on the programs guess.
            userFeedback = input(f'\nIs {compGuess} your number?\nGo Higher (H), Go Lower (L), Yes (Y) ').lower()
            if userFeedback == "h":
                # Adjusting the lowerbound of the guessing range.
                goHigh = compGuess+1

            elif userFeedback == "l":
                # Adjusting the upperbound of the guessing range.
                goLow = compGuess - 1

            # Counting the number of iterations through the loop, i.e. the number of guesses.
            countGuess = countGuess + 1

        # After the program has guessed the number correctly, the while loop breaks.
        print(f'\nThe computer has guessed the number {compGuess} correctly!'
            f'\nIt took the computer {countGuess} guesses!')

        # Asking the user whether they would like to play again.
        playAgain = input("\nWould you like to play again? (Y/N)\n").lower()
        if playAgain == "y":
            # If the user says yes, all the variables are initialised again.
            goLow = 100
            goHigh = 1
            userFeedback = ''
            countGuess = 0

    # If the user doesn't want to play anymore, the main while loop breaks, and the function ends.
    print("\nThanks for playing!")

# Running the function.
guessNum()