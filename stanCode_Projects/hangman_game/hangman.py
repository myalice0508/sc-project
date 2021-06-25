"""
File: hangman.py
Name: Irene Chen 陳筱涵
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    pre-condition: To guess the word.
    post-condition: Guess the word, but if the guess isn't match the word, will be reduce the life.
                    And just can input the one alphabet, and can't input the digital.
    """
    word = random_word()
    unknown = "-"
    your_guess = unknown * len(word)
    print("The word looks like: " + your_guess)
    print('You have ' + str(N_TURNS) + ' guesses left.')
    life = N_TURNS

    while True:
        guess = str(input('Your guess: '))
        if len(guess) == 1 and guess.isalpha():
            if word.find(guess.upper()) == -1:
                life -= 1
                print('There is no ' + guess.upper() + "'s in the word.")
                print('The word looks like: ' + your_guess)
                print('You have '+str(life)+' guesses left.')
            else:
                ret = replace(your_guess, unknown, guess, word)
                your_guess = ret.upper()
                print('You are correct')
                print('The word looks like: ' + your_guess)
                print('You have ' + str(life) + ' guesses left.')
            if life == 0:
                print('you dead')
                break
            if your_guess == word:
                print('You are correct !')
                print('You win !')
                print('The word was: ' + your_guess)
                break
        else:
            print('illegal format')


def replace(your_guess, unknown, guess, word):
        """
        post- condition: Your guess will be replaced with correct guess
        """
        i = word.find(guess.upper())
        j = word[i + 1:].find(guess.upper())
        k = word[i+1+j+1:].find(guess.upper())
        ans = ''
        ans += your_guess[:i]
        ans += guess.upper()
        if j == -1:
            ans += your_guess[i+1:]
            return ans
        else:
            # if the word has two guess alphabets.
            ans += your_guess[i+1:i+1+j]
            ans += guess.upper()
            if k == -1:
                ans += your_guess[i+1+j+1:]
                return ans
            else:
                # if the word has three guess alphabets.
                ans += your_guess[i+1+j+1:i+1+j+1+k]
                ans += guess.upper()
                ans += your_guess[i+1+j+1+k+1:]
                return ans




def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
