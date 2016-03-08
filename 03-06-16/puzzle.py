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

ROW1 = 'qwertyuiop'
ROW2 = 'asdfghjkl'
ROW3 = 'zxcvbnm'

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

    for i in range(len(four_chars)-4):
        if (four_chars[i][0:3] == four_chars[i+1][0:3]) and (four_chars[i][0:3] == four_chars[i+2][0:3]) and\
                (four_chars[i][0:3] == four_chars[i+3][0:3]) and (four_chars[i][0:3] == four_chars[i+4][0:3]):
            if (four_chars[i][3] in ROW2) and (four_chars[i+1][3] in ROW2) and (four_chars[i+2][3] in ROW2) and\
                    (four_chars[i+3][3] in ROW2) and (four_chars[i+4][3] in ROW2):
                print(four_chars[i][::-1], four_chars[i+1][::-1], four_chars[i+2][::-1], four_chars[i+3][::-1],
                    four_chars[i+4][::-1])




# Check for interactive session
if __name__ == '__main__':
    # execute main program
    main()
