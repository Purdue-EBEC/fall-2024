"""
Author: John Cole, jhcole@purdue.edu
Assignment: 06.4 - Spiral
Date: 09/27/2021

Description:
    This program draws an Archimedean spiral pattern.

Contributors:
    None

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

from turtle import *

"""Import additional modules below this line (starting with unit 6)."""
from math import cos, pi, sin, tau

"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function.
    """
    setup(564, 564)
    width(5)


def main():
    # Draw six turns of the spiral
    for degrees in range(0, 6 * 360 + 1):
        # Calculate new x and y coordinates
        radius = degrees / pi**2
        radians = degrees * tau / 360
        x, y = radius * cos(radians), radius * sin(radians)
        goto(x, y)
    """getcanvas().postscript(file='spiral_archimedean.eps')"""


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
