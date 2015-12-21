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

    for i in range(num_words):
        num_chars = len(words[i])
        # Not worrying about excluding things that begin with uppercase
        for j in range(num_chars-2):
            if ((ord(words[i][j])+1) == ord(words[i][j+1])) and ((ord(words[i][j])+2) == ord(words[i][j+2])):
                print(words[i], end="")
                break



# Check for interactive session
if __name__ == '__main__':
    # execute main program
    main()
