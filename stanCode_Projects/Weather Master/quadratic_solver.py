"""
File: quadratic_solver.py
Name: Irene Chen 陳筱涵
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
    """
    pre-condition: make three Variable and input the number from the user
    post-condition: to calculate the quadratic solver.
    """
    print('stanCode Quadratic Solver!')
    n1 = int(input('a: '))
    n2 = int(input('b: '))
    n3 = int(input('c: '))

    x = (n2 * n2) - (4 * n1 * n3)
    y = my_calculate(x)
    z1 = (-n2 + y) / 2 * n1
    z2 = (-n2 - y) / 2 * n1
    z3 = -n2 / (2 * n1)

    if x < 0:
        print('No real roots')

    elif x == 0:
        print(float(z3))

    else:
        print(str(float(z1)) + ',' + str(float(z2)))


def my_calculate(x):
    """
    :param x: The word to be calculate
    :return result: The math.sqrt result
    """

    if x < 0:
        return 0
    return math.sqrt(x)


	


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
