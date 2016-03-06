"""Playing around with Python to do the Sunday Puzzle

Sunday puzzle from Mar, 6, 2016:
TBail, Nail, and Mail are three four-letter words that differ only by their first
letters. And those first letters (B, N, and M) happen to be adjacent on a computer
keyboard. Can you think of five four-letter words that have the same property —
that is, they're identical except for their first letters, with those first letters
being adjacent on the keyboard? All five words must be ones that everyone knows.
Capitalized words and plurals are not allowed. What words are they?



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
        if (num_chars == 6):
            print(words[i])
        # Not worrying about excluding things that begin with uppercase
        # for j in range(num_chars-2):
        #     if ((ord(words[i][j])+1) == ord(words[i][j+1])) and ((ord(words[i][j])+2) == ord(words[i][j+2])):
        #         print(words[i], end="")
        #         break



# Check for interactive session
if __name__ == '__main__':
    # execute main program
    main()
