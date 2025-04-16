"""
Lab - Object Oriented Programming (OOP)
By: Garrett Kolenbrander

CSCI 110
Date: 16/4/25

Object Oriented Programming:
Using user-defined class/type, program finds area and 
circumference of a circle.
"""

import math


class Circle(object):
    """
    Class that represents a circle with three attributes – radius, area and circumference.
    Class has two user-defined methods findArea and findCirumference and two special 
    built-in methods:   __init__ and __str__.
    """

    def __init__(self, r=0):
        self.radius = r
        self.area = self.findArea()
        self.circumference = self.findCircumference()

    def findArea(self):
        return math.pi*(self.radius**2)

    def findCircumference(self):
        return math.pi * (self.radius * 2)

    def __str__(self):
        return "Circle - radius: {:.2f}, area: {:.2f} circumference: {:.2f}".format(self.radius, self.area, self.circumference)


def main():
    # instantiate aCir object with radius 1
    aCir = Circle(1)
    print(aCir)
    # FIXME3: (20 pts)
    # Instantiate another circle with radius 5
    bCir = Circle(5)
    # Print the circle
    print(bCir)

    # FIMXE4: (20 pts)
    # prompt user to enter radius and store into a variable
    user_raduis = input("Enter the radius of the circle: ")

    # FIXME5: (20 pts)
    # create a circle with the user provided radius
    # print the circle
    user_circle = Circle(int(user_raduis))
    print(user_circle)


if __name__ == "__main__":
    main()
