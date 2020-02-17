"""Playing around with Python to solve the NPR Sunday Puzzle for 2019-09-29

What familiar 10-letter word contains a silent B, E, and O — not necessarily
in that order. And those three letters don't have to be consecutive in the word.

"""

import sys, logging


__author__ = 'rnzucker'

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

ALPHABET ='abcdefghijklmnopqrstuvwxyz'


def main():
    word_file = open("words.txt", "r")
    # Switched to using longer word file
    # word_file = open("../03-06-16/long-wordsEn.txt", "r")
    words = word_file.readlines()
    num_words = len(words)
    print("There are {} words.\n".format(num_words))

    for i in range(num_words):
        num_chars = len(words[i])
        if num_chars==11: # Newline is included in the number of characters. Must be at least five characters
            if ((words[i].find('b') != -1) and (words[i].find('e') != -1) and
                (words[i].find('o') != -1)):
                print(words[i].rstrip())



# Check for interactive session
if __name__ == '__main__':
    # execute main program
    main()
