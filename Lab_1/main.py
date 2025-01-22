"""
    StdIO Lab
    ASCII Art - using literals and variables
    
    Updated By: Garrett Kolenbrander #FIXED
    Date: 21/1/25 #FIXED
    
    This program produces an ASCII art on the console.

    Algorithm steps: 
    1. Use variables to store data/values
    2. Write a series of print statements to print the data/values to the console
"""
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

print("Welcome to ASCII Art Program...\n")

username: str = input("What is your name? ") #FIXED
print("Nice meeting you, ", username, "!\n") #FIXED
# must output: Nice meeting you, <name>!

# prompt user to enter the semester and store the value into semester variable using input function
semester: str = input("What semester is this [Fall/Spring]? ")
print("This is " + semester + " semester.\n")

year: str = input("Enter the year: ") #FIXED
print("This is", year, "year.\n") #FIXED
# must output: This is <year> year.

print("Hope you like my ASCII art...\n\n")

line1: str = "  |\\_/|   **********************    (\\_/)"
print(line1)

line2: str = " / @ @ \  *      ASCII Lab     *   (='.'=)"
print(line2) #FIXED7

print('( > 0 < ) *      Garrett       * ( " )_( " )') #FIXED8

line4: str  = '  >>x<<   *      CSCI 110      *'
print(line4) #FIXED9

line5: str = ' /  O  \  **********************' #FIXED10
print(line5)

print("\nGood bye...  \n")