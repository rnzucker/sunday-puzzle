"""Playing around with Python to solve the NPR Sunday Puzzle

Take the word EASY: Its first three letters: E, A, and S, are the fifth
first, and nineteenth letters, respectively, in the alphabet. If you add
5 + 1 + 19, you get 25, which is the value of the alphabetical position
of Y, the last letter of EASY.

Can you think of a common five-letter word that works in the opposite way
- in which the value of the alphabetical positions of its last four letters
add up to the value of the alphabetical position of its first letter?
This is part of solving the NPR Sunday Puzzle for Apr. 3, 2016
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
        if num_chars==6: # Newline is included in the number of characters
            # Remove \n
            temp = words[i][0:6].rstrip()
            # Find the number value of each letter
            num_1 = ALPHABET.find(temp[0]) + 1
            num_2 = ALPHABET.find(temp[1]) + 1
            num_3 = ALPHABET.find(temp[2]) + 1
            num_4 = ALPHABET.find(temp[3]) + 1
            num_5 = ALPHABET.find(temp[4]) + 1
            if num_1 == (num_2 + num_3 + num_4 + num_5):
                print(temp)


# Check for interactive session
if __name__ == '__main__':
    # execute main program
    main()
