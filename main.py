# Password Generator Script for use generically at home.
# Written by Harry Perriton

from random import choice
from time import sleep
from os import system

PROGRAM_ON = True
while PROGRAM_ON:

    AVAILABLE_CHARACTERS = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_*!?$')
    OUTPUT_ANSWER = ""

    print("Welcome to password generator script 1.0!")
    sleep(2)

    # Use while loop to check user's input validity.
    check_input = True
    while check_input:
        # Take the user input so that you know how many characters the password should contain.
        character_number_input = input("How many characters would you like your password to contain? ")
        if character_number_input == "":
            print("Error: Please enter a whole number between 8 and 20!")
            sleep(2)
            system('cls')

        else:
            # Next check to see that the input is actually a number.
            try:
                character_number_input = int(character_number_input)
            except:
                print("Error: Please enter an integer number between 8 and 20!")

            # Catch if the number being used is too big or too small, generally websites have limits.
            if character_number_input > 20 or character_number_input < 8:
                print("Error: Please enter an integer number between 8 and 20!")

            else:
                # Use a for loop to create a password in the range of characters as specified by the user.
                for i in range(character_number_input):
                    new_char = choice(AVAILABLE_CHARACTERS)
                    OUTPUT_ANSWER += new_char

                # Output the password on the screen.
                print("Here is your new password:")
                print(OUTPUT_ANSWER)
                check_input = False

    # Check whether the user wants to use the application again.
    redo_check = True
    while redo_check:
        # Take input and check it for binary answer, base case is always error.
        player_redo_input = input("Would you like to make another password? (Yes/No) ")
        match player_redo_input.lower():
            case "yes":
                redo_check = False
                PROGRAM_ON = True
                sleep(3)
                system('cls')
            case "no":
                print("Thankyou for using Password Generator Script 1.0!")
                sleep(3)
                redo_check = False
                PROGRAM_ON = False
            case _:
                print("Error: Please pick a valid option of yes or no.")
                sleep(2)
                system('cls')
