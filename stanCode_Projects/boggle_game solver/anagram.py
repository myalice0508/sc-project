"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global Variable
dictionary = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def main():
    print(f'Welcome to stanCode "Anagram Generator" (or -1 to quit')
    word = str(input('Find anagrams for:'))
    if word == EXIT:
        pass
    else:
        read_dictionary()
        a = find_anagrams(word)
        for word in a:
            print('Searching...')
            print(f'Found: {word}')


def read_dictionary():

    with open(FILE,'r') as f:
        for line in f:
            word = line.strip()
            dictionary.append(word)

    return dictionary


def find_anagrams(s):
    """
    :param s:
    :return:
    """

    letter_l = []

    for letter in s:
        letter_l.append(letter)

    return word_helper(s,letter_l, [], "", [])


def word_helper(s, word, word_lst, the_word, find_lst):


    #Base case:
    if len(word) == 0:
        if the_word not in find_lst:
            if the_word in dictionary:
                find_lst.append(the_word)
    else:
        for word_letter in s:
            if word_letter not in the_word or word_letter in word:
                word.remove(word_letter)
                the_word += word_letter
                if has_prefix(the_word):
                    # Explore
                    word_helper(s, word, word_lst, the_word, find_lst)
                the_word = the_word[0:-1]
                word.append(word_letter)

    return find_lst


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """

    for word in dictionary:
        if word.startswith(sub_s):
            return True
    return False

if __name__ == '__main__':
    main()
