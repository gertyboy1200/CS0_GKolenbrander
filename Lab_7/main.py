
"""
CSCI 110
List Lab

By: Garrett Kolenrbander
Date: 10/4/25

Program prompts user to enter 10 integers and stores the entered numbers into a list.
Program will then sort the numbers in the list in ascending and descending orders
and print the largest and smallest values in the list.
Program will also print the indices of the largest and smallest numbers in the list.
"""

totalInts = 10

def getIntegers():
    intList = []
    i = 0
    while i < totalInts:
        num = int(input("Enter an integer: "))
        intList.append(num)
        i += 1
    return intList


def sortListInAscendingOrder(intList):
    intList.sort()


def sortListInDescendingOrder(intList):
    intList.sort(reverse = True) #GeeksforGeeks python sort method https://www.geeksforgeeks.org/python-list-sort-method/


def printList(intList):
    for val in intList:
        print(val, end=' ')
    print()


def find_largest_number(int_list):
    sortListInAscendingOrder(int_list)
    return int_list[-1]

def find_smallest_number(int_list):
    sortListInDescendingOrder(int_list)
    return int_list[-1]



def main():
    integers = []  # empty list to store integers
    integers = getIntegers()
    original_list = list(integers)
    print("Numbers entered are: ")
    printList(integers)

    # sort numbers
    sortListInAscendingOrder(integers)
    print("Numbers in ascending order: ")
    printList(integers)

    # FIXME4 (10 points)
    # Call sortListInDescendingOrder function
    sortListInDescendingOrder(integers) #FIXED

    # FIXME5 (10 points)
    # Print the sorted list in descending order
    print("Numbers in decending order: ")
    printList(integers) #FIXED

    # FIXME6 (10 points)
    # Print the largest number
    print("the largest number is: ")
    largest_number = find_largest_number(integers)
    print(largest_number) #FIXED

    # FIXME7 (10 points)
    # Print the smallest number
    print("the smallest number is: ")
    smallest_number = find_smallest_number(integers)
    print(smallest_number) #FIXED

    # FIXME8 (10 points)
    # Find and print the index of the smallest number
    print("the index of the smallest number is:")
    print(original_list.index(smallest_number)) #FIXED

    # FIXME9 (10 points)
    # Print the index of the largest number
    print("the index of the largest number is:")
    print(original_list.index(largest_number)) #FIXED

#FIXED10
if __name__ == "__main__":
    main()

