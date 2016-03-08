"""Playing around with Python to do the Sunday Puzzle

Sunday puzzle from Mar, 6, 2016:
Bail, Nail, and Mail are three four-letter words that differ only by their first
letters. And those first letters (B, N, and M) happen to be adjacent on a computer
keyboard. Can you think of five four-letter words that have the same property —
that is, they're identical except for their first letters, with those first letters
being adjacent on the keyboard? All five words must be ones that everyone knows.
Capitalized words and plurals are not allowed. What words are they?

Part of solution involves scanning words file for 4-letter words and creating
a new list with the words, but with the letter order reversed.

"""

import sys, logging


__author__ = 'rnzucker'

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

ROW1 = 'qwertyuiop'  # Letters, in order, in first row of keyboard
ROW2 = 'asdfghjkl'   # Letters, in order, in second row of keyboard
ROW3 = 'zxcvbnm'     # Letters, in order, in third row of keyboard

def all_in_same_row(word_list, i, row):
    """ Return true if fourth (really, first) letter of this and next four words in this row

    :param word_list: The list of four letter words (reversed)
    :param i: index where this word and the next four have same first three (really, last) letters
    :param row: A string of the letters in one keyboard row
    :return: True if all the reversed words end with letters in this keyboard row
    """
    if (word_list[i][3] in row) and (word_list[i+1][3] in row) and (word_list[i+2][3] in row) and\
            (word_list[i+3][3] in row) and (word_list[i+4][3] in row):
        return True

def main():
    #
    # word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    # word_list = requests.get(word_site)
    # words = word_list.content.splitlines()
    word_file = open("long-wordsEn.txt", "r")
    words = word_file.readlines()
    num_words = len(words)
    print("There are {} words.\n".format(num_words))

    j = 0
    four_chars = []
    for i in range(num_words):
        num_chars = len(words[i])
        if (num_chars ==5): # Newline is included in the number of characters
            # Remove \n
            temp = words[i][0:4].rstrip()
            # Append reverse form of word to end
            four_chars.append(temp[::-1])
            # print(four_chars[j])
            j = j + 1
    print("\n", j, "four letter words\n")
    four_chars.sort()
    # print(four_chars)

    # Check first three letters (in reversed form) of five consecutive words to see if they match.
    # Then check to see if the fourth (actually first) letters are all in the same row of the keyboard
    # by checking set membership in ROW1, ROW2, or ROW3.
    for i in range(len(four_chars)-4):
        if (four_chars[i][0:3] == four_chars[i+1][0:3]) and (four_chars[i][0:3] == four_chars[i+2][0:3]) and\
                (four_chars[i][0:3] == four_chars[i+3][0:3]) and (four_chars[i][0:3] == four_chars[i+4][0:3]):
            if all_in_same_row(four_chars, i, ROW1) or all_in_same_row(four_chars, i, ROW2) or\
                    all_in_same_row(four_chars, i, ROW3):
                print(four_chars[i][::-1], four_chars[i+1][::-1], four_chars[i+2][::-1], four_chars[i+3][::-1],
                    four_chars[i+4][::-1])





# Check for interactive session
if __name__ == '__main__':
    # execute main program
    main()
