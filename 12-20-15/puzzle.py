"""Playing around with Python text modules to do MadLibs

This will look through a list of words in a file to find any
that have three consecutive letters in adjacent alphabetical
order. An example are "n", "o", and "p" in "canopy". This is
part of solving the NPR Sunday Puzzle for Nov. 11, 2015

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
    six_words = []
    for i in range(num_words):
        num_chars = len(words[i])
        if (num_chars ==7): # Newline is included in the number of characters
            # Remove \n
            temp = words[i][0:6].rstrip()
            # Append reverse form of word to end
            six_words.append(temp[::-1])
            print(six_words[j])
            j = j + 1
    print("\n", j, "six letter words")
    six_words.sort()
    # print(six_words)

    for i in range(len(six_words)-3):
        if (six_words[i][0:5] == six_words[i+1][0:5]) and (six_words[i][0:5] == six_words[i+2][0:5]) and\
                (six_words[i][0:5] == six_words[i+3][0:5]):
            print(six_words[i][::-1], six_words[i+1][::-1], six_words[i+2][::-1], six_words[i+3][::-1])




# Check for interactive session
if __name__ == '__main__':
    # execute main program
    main()
