###
# Functions Lab
# Updated By: Garrett Kolenbrander FIXED 1
#
# CSCI 110
# Date: 18/2/2025 FIXED 2
###

someName = "Bill Gates"

myName = "Garrett Kolenbrander" # FIXED 3

def printHello():
    """
    function that prints Hello World.
    doesn't take any argument and doesn't return a value
    """
    print("Hello World!")

def printHelloTwice():
    """
    # function that prints Hello World twice
    # calls printHello function twice
    """
    printHello()
    printHello()

def greetName(name):
    """ 
    function that takes one argument name and greets the name
    """
    print("Hi there {}".format(name))

def meetAndGreet():
    """
    function that greets someone
    doesn't take any argument and doesn't return any value
    """
    firstName = input("\nHey there! what's your first name?\n")
    # firstName is local variable
    greetName(firstName)  # call greetName function
    print("My name is {}. Nice meeting you.".format(myName))
    print()  # print empty line

def convertTime(seconds):
    """
    Define a function named convertTime that takes 1 integer argument called seconds.
    The function converts and prints the seconds in hours, minute, and seconds formats.
    """
    hour = seconds//3600
    # seconds = seconds%3600
    # seconds = seconds-hour*3600;
    m = seconds//60
    m = m % 60
    sec = seconds % 60
    #seconds = seconds - m*60
    print("{} seconds = {} hours, {} minutes, {} seconds".format(seconds, hour, m, sec))


def findSeconds(hours):
    """
    Define a function named findSeconds that takes hours as 1 integer argument.
    The function converts hours into seconds and returns it
    """
    seconds = hours * 3600 # FIXED 4
    return seconds


def testFunctions():
    # test1 : # for 1 hour == 3600 seconds
    assert(findSeconds(1) == 3600)

    # test2 : # for 2 hour == 7200 seconds
    assert(findSeconds(2) == 7200)

    # test3 : # for 4 hour == 14400 seconds
    assert(findSeconds(4) == 14400)

    # test4 : # for 24 hour == 86400 seconds
    assert(findSeconds(24) == 86400)

    print('all test cases passed...')


printHello() #FIXED 6

printHelloTwice() # FIXED 7

greetName(someName)
greetName("Larry Page")

meetAndGreet()

convertTime(60)

convertTime(3600) # FIXED 8

convertTime(3661) # FIXED 9

testFunctions() # FIXDE 10
