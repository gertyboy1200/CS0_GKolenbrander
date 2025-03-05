"""
Lab - Playing with Loops
Updated By: Garrett Kolenbrander
CSCI 110
Date: 5/3/25
Program prints geometric shapes of given height with * using loops
"""
import os
import sys

def print_triangle(height):
    for i in range(1, height + 1):
        print("* " * i)
    print()

def print_flipped_triangle(height): # FIXED 3
    for i in range(height, 0, -1):
        print("* " * i)
    print()

# FIXED 4
def print_square(height):
    for i in range(1, height + 1):
        print("* " * height)
    print()

def clear_screen():
    """
    function to clear screen based on the operating system
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    # FIXED 7
    while True:
        clear_screen()
        print('Program prints geometric shapes of given height with *')
        height = int(input('Please enter the height of the shape: '))
        print_triangle(height)

        # FIXED 5
        print_flipped_triangle(height)

        # FIXED 6
        print_square(height)

        # FIXME9
        user_input = input("Enter 'y/Y' to continue: ")

        # FIXME10
        if user_input == 'y' or user_input == 'Y': #FIXED 8
            continue 
        else:
            print("EXITING!!!!!!")
            break

if __name__ == "__main__":
    main()