"""Playing around with Python to solve the NPR Sunday Puzzle for 2019-09-29

Think of a word that has five vowels — two E's, an I, O, and U. Curiously,
every vowel except the "I" is pronounced like a short "I." And the "I" in
the word is not pronounced at all. What word is it?

This should print out every word that has exactly two E's, and one I, one O,
and one U. From there the reader must eyeball it.

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
        if num_chars>=6: # Newline is included in the number of characters. Must be at least five characters
            if ((words[i].find('i') != -1) and (words[i].find('o') != -1) and
                (words[i].find('u') != -1) and (words[i].find('e') != -1) and (words[i].find('a') == -1)):
                first_e = words[i].find('e')
                if (words[i].find('e', first_e+1) != -1):
                    # Know that there is at least one character after the first 'e' due to the newline
                    # Know that there are at least two e's. There could be more than two though. Should be fixed.
                    if ((words[i].find('i') == words[i].rfind('i')) and (words[i].find('o') == words[i].rfind('o')) and
                        (words[i].find('u') == words[i].rfind('u'))):
                        # Making sure there is only one i, o, and u
                        print(words[i].rstrip())



# Check for interactive session
if __name__ == '__main__':
    # execute main program
    main()
