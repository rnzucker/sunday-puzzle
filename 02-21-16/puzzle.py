"""Playing around with Python text modules to do MadLibs

three eight-letter words that are identical in spelling except for
the fourth letter. Each word contains a G that is pronounced
differently in all three words.
This is part of solving the NPR Sunday Puzzle for Feb. 21, 2016

"""

import sys, logging


__author__ = 'rnzucker'

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


def main():
    #
    # word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    # word_list = requests.get(word_site)
    # words = word_list.content.splitlines()
    word_file = open("words.txt", "r")
    words = word_file.readlines()
    num_words = len(words)
    print("There are {} words.\n".format(num_words))

    j = 0
    eight_words = []
    for i in range(num_words):
        num_chars = len(words[i])
        if (num_chars ==9): # Newline is included in the number of characters
            # Remove \n
            temp = words[i][0:6].rstrip()
            # Append reverse form of word to end
            eight_words.append(temp[::-1])
            print(eight_words[j])
            j = j + 1
    print("\n", j, "eight letter words")
    eight_words.sort()
    # print(eight_words)

    for i in range(len(eight_words)-3):
        if (eight_words[i][0:5] == eight_words[i+1][0:5]) and (eight_words[i][0:5] == eight_words[i+2][0:5]) and\
                (eight_words[i][0:5] == eight_words[i+3][0:5]):
            print(eight_words[i][::-1], eight_words[i+1][::-1], eight_words[i+2][::-1], eight_words[i+3][::-1])




# Check for interactive session
if __name__ == '__main__':
    # execute main program
    main()
