"""
Lab - Conditional Statements

By: Garrett Kolenbrander

CSCI 110
Date: 26/2/25

Program prompts user to enter a number and determines whether the entered number is even or odd, positive or negative or zero.

Algorithm steps:
1. Prompt user to enter a number
2. Convert the value into integer and store it into a variable
3. Define a function that takes a number as parameter and determines whether the number is
even or odd using the following algorithm:
    3.1 If the number is divisible by 2 with the remainder 0, it is an even number
    3.2 Otherwise, it is an odd number
    3.3 The function returns True for even and False for odd number

4. Define a function that takes a number as parameter and determines whether the number is positive or not using the following algorithm:
	4.1 If the number is greater than zero, return True
	4.2 Otherwise, return False

5. Define a function that takes a number as parameter and determines whether the number is zero or not using the following algorithm:
    5.1 If the number = 0, return True
    5.2 Otherwise, return False
6. Call the functions using the entered number and display the results with proper descriptions.
7. Test and validate the program output is correct with several different numbers
"""

import sys
import os

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def is_positive(num):
    if num > 0:
        return True
    else:
        return False

def is_zero(num):
    if num == 0:
        return True
    else:
        return False

def greet_user(user_name): # FIXED 5
    print("hello,", user_name, "welcome onboard!")
# Define a function that takes in a string name argument
# function greets the name by printing, e.g.: Hello, John! Welcome onboard...

def clear_screen():
    """
    function that clears the console/terminal
    """
    if os.name == 'nt': # if os is windows
        os.system('cls') # run cls command
    else:
        os.system('clear')  # run clear command

def main():
    """
    main program
    """
    clear_screen() # clear screen
    print("Program determines whether a given number is even or odd")
    ans = input('Do you want to continue? Enter [y|n]: ')
    if ans != 'y':
        sys.exit()  # exit/end the program

    user_name = input("Please enter your name: ") # FIXED 6

    # loop until user wants to quit
    while True:
        # clear the screen for subsequent use
        clear_screen()
        greet_user(user_name)
        print("Enter a whole number, {}:".format(user_name))
        user_input = input()
        if not user_input.strip('-').isdecimal():
            print('Not a number, enter to continue...')
            input()
            continue

        user_input = int(user_input)
        if is_zero(user_input):
            print(user_input, "is zero!")
        else:
            # Call isEven function and store the returned value into even variable
            even = is_even(user_input)
            if even:
                print(user_input, "is an even number!")
            else:
                print(user_input, "is an odd number!")

            positive = is_positive(user_input) # FIXED 8
            if positive:
                print(user_input, "is positive!")
            else:
                print(user_input, "is negative!")

        answer = input(
            "Would you like to check another number? Enter y or yes; anything else to quit: ")
        if answer == 'y' or answer == 'yes': # FIXED 9
            continue

        else:
            print('Thanks for using the program, {}! Good bye...'.format(user_name))
            break

def test():
    assert is_positive(99) == True
    assert is_even(12) == True
    assert is_zero(0) == True
    print('all test cases passed...')
    print('press enter to continue')
    input()

test() # FIXED 10

main()