"""
File: hailstone.py
Name: Irene Chen 陳筱涵
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    pre-condition: give a number to the request " Enter the number"
    post-condition: to make some calculation until the result to be one.
                    (if the number is odd, making 3n+1 or taking half)
    """

    print('This program computes Hailstone sequences.')

    number = int(input('Enter the number: '))

    if number == 1:
        print('It took 0 steps to reach 1.')
    else:
        step = 0
        while True:
            if number == 1:
                break
            if number % 2 == 1:
                number = number * 3 + 1
                print(str(int((number - 1) / 3))+' is odd,  so I make 3n+1: '+str(int(number)))
            elif number % 2 == 0:
                number = number / 2
                print(str(int(number * 2)) + ' is even,  so I take half: ' + str(int(number)))
            if number != 0:
                step += 1
                # added the calculated step
        print('It took ' + str(step) + ' steps to reach 1.')




###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
