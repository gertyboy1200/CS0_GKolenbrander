"""
File I/O Lab
By: Garrett Kolenbrander

CSCI 110
Date: 15/4/25

Program prompts user to enter name of the file that contains 10 integers.
It opens, reads and stores the numbers into a list.
Program will then sort the numbers in the list in ascending and descending orders
Program will then print the sorted lists to an output file along with the 
largest and smallest values in the list.

NOTE: All fixme's are each worth 10 points except for the FIXME1 which is worth 20 points
"""


def readData():
    intList = []

    file_name = input("Enter the name of the file you wish to open: ")
    with open(file_name, 'r') as file:
        for line in file:
            intList.append(int(line))

    file.close()
    return intList


def sortListInAscendingOrder(lstInts):
    lstInts.sort()



def sortListInDescendingOrder(lstInts):

    lstInts.sort(reverse = True)


def printList(printFile, lstInts):
    for i in lstInts:
        printFile.write(str(i) + '\n')


def main():
    integers = []  # list to store integers
    integers = readData()
    outputFileName = input('Enter a file to write output to: ')
    printFile = open(outputFileName, 'w')
    printFile.write("Numbers entered:\n")
    printList(printFile, integers)

    sortListInAscendingOrder(integers)
    printFile.write("Numbers sorted in ascending order:\n")
    printList(printFile, integers)

    sortListInDescendingOrder(integers)
    printFile.write("Numbers sorted in descending order:\n")
    printList(printFile, integers)

    printFile.write("the largest number in the file is:\n")
    sortListInDescendingOrder(integers)
    printFile.write(str(integers[0]) + "\n")

    printFile.write("the smallest number in the file is:\n")
    sortListInAscendingOrder(integers)
    printFile.write(str(integers[0]) + "\n")

    printFile.close()
    print('Done executing the program! Check the output file for results.')


if __name__ == "__main__":
    main()
