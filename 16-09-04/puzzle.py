"""Playing around with Python to solve the NPR Sunday Puzzle

Take the letters R and N. As lower-case letters, when adjacent, they look
like the letter M (rn versus m).

Can you think of a common five-letter word with the letters R and N adjacent,
where those two are changed to an M, you get a word with the opposite meaning?

This is part of solving the NPR Sunday Puzzle for Sept. 4, 2016
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
            for j in range(len(temp)-1):
                if (temp[j] == 'r') and (temp[j+1] == 'n'):
                    print(temp,)



# Check for interactive session
if __name__ == '__main__':
    # execute main program
    main()
