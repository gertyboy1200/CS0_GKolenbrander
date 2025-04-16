"""
File I/O Lab with Dictionary

Update By: Garrett Kolenbrander

CSCI 110
Date: 16/4/25

Program finds the frequency of words in a given text document and print top 10 most
common words using dictionary and tuple data structures.
"""

def readText():
    """
    Opens a file, reads its contents, and
    creates a histogram of words based on frequency using a dictionary data structure.
    """
    fileOk = False
    fin = None
    hist = {}

    while not fileOk:
        fileName = input('Enter input text file => ')
        try:
            fin = open(fileName, 'r')
            fileOk = True
        except Exception as ex:
            print('Exception occurred:', ex)

    lines = fin.readlines()
    for line in lines:
        line = line.strip().lower()

        if line:
            words = line.split()
            for word in words:
                if word in hist:
                    hist[word] += 1
                else:
                    hist[word] = 1 

    fin.close()
    return hist


def reverseHistogramList(histDict):
    reverseList = []
    for key, val in histDict.items():
        reverseList.append((val, key))

    reverseList.sort(reverse=True)
    return reverseList


def main():
    histogram = readText()

    aList = reverseHistogramList(histogram)

    # Print top 10 words with highest frequencies
    print("Top 10 most common words:")
    for i in range(min(10, len(aList))):
        count, word = aList[i]
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
