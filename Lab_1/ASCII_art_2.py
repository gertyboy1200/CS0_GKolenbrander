"""
    StdIO Lab 1B
    ASCII Art 2 - using literals and variables
    
    Updated By: <Garrett Kolenbrander> #FIXED 1
    Date: 1/2/25 #FIXED 2
    
    This program produces an ASCII art on the console.
    It should look something like this.


         /\         ************************************************************      /~~   ~~\
        /##\                                                                       /~~         ~~\
       /#""#\                               Ascii Art 2                           {               }
      /#"##"#\                                 CS110                               \  _-     -_  /
     /#"#""#"#\                              Spring 25                              ~  \\   //  ~
    /#"#CMU!#"#\                            Corin Chepko                          _- -   | | _- _
         ||                                                                         _ -  | |   -_
         ||         ************************************************************        // \\

    Algorithm steps: 
    1. Use variables to store art and data
    2. Write a series of print statements to print the data/values to the console, using the .center() method
        to keep the strings centered.
    
    Note: You can add more lines or print differt ASCII arts of your choice if you'd like...
"""
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
print("Welcome to ASCII Art Program...\n")

#FIXED 3
username = input("Please enter your name: ")
print("Nice meeting you, ", username, "!\n")

semester = input("What semester is this [Fall/Spring]? ")

#FIXED 5
course_name = input("please enter your course name: ")

#FIXED 6
lab_title = input("Pleas enter your lab title: ")

print("Hope you like my ASCII art...\n\n")

left_width = 20
right_width = 20
center_width = 40 

#FIXED 7-8
treeA_1 = '      /\        '
treeA_2 = '     /##\       '
treeA_3 = '    /#""#\      '
treeA_4 = '   /#"##"#\     '
treeA_5 = '  /#"#""#"#\    '
treeA_6 = ' /#"#CMU!#"#\   '
treeA_7 = '      ||        '
treeA_8 = '      ||        '

treeB_1 = '     /~~   ~~\     '
treeB_2 = '  /~~         ~~\  '
treeB_3 = '{                 }'
treeB_4 = '  \  _-     -_  /  '
treeB_5 = '   ~  \\   //  ~   '
treeB_6 = ' _- -   | | _- _   '
treeB_7 = '   _ -  | |   -_   '
treeB_8 = '       // \\       '

asterics: str = "*"*center_width
spaces: str = " "*center_width

#FIXED 9-10
print(treeA_1.center(left_width) + asterics.center(center_width) + treeB_1.center(right_width))
print(treeA_2.center(left_width) + spaces.center(center_width) + treeB_2.center(right_width))
print(treeA_3.center(left_width) + lab_title.center(center_width) + treeB_3.center(right_width))
print(treeA_4.center(left_width) + course_name.center(center_width) + treeB_4.center(right_width))
print(treeA_5.center(left_width) + semester.center(center_width) + treeB_5.center(right_width))
print(treeA_6.center(left_width) + username.center(center_width) + treeB_6.center(right_width))
print(treeA_7.center(left_width) + spaces.center(center_width) + treeB_7.center(right_width))
print(treeA_8.center(left_width) + asterics.center(center_width) + treeB_8.center(right_width))

print("\nGood bye...  \n")