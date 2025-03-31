"""
Strings and Unittest Lab
Updated By: Garrett Kolenbrander
CSCI 110 Lab
Date: 30/3/25

Read and solve - Simon Says: https://open.kattis.com/problems/simonsays  

Algorithm:
    1. Read N
    2. Repeat N times:
        1. Read the input string
        2. Check if the string begins with 'Simon says'
        3. If it does, print the rest of the string after 'Simon says', otherwise ignore the string
"""

from typing import Union


def main():
    """Main function that solves the problem.
    """
    N = int(input())

    for i in range (0, N):
        command = input()
        answer(command)
        if answer(command) == None:
            continue
        else:
            print(answer(command))



def valid_command(command: str) -> bool:
    """Checks if the string starts with 'Simon says'.

    Args:
        command (str): string to check.

    Returns:
        bool: True if the string starts with 'Simon says', False otherwise.
    """
    if "Simon says" in command:
        ans = True
    else:
        ans = False
    return ans


def answer(command: str) -> Union[str, None]:
    """Returns answer given the command or None if the command is not valid.

    Args:
        command (str): string to check

    Returns:
        str|None: rest of the string after 'Simon says' if the command is valid, None otherwise
    """
    valid = valid_command(command)
    if valid:
        return command[10:] # using substrings
    else:
        return None


if __name__ == "__main__":
    # call the main function if the script is run from the command line
    main()
