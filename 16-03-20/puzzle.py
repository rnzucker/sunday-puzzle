"""Playing around with Python to solve the NPR Sunday Puzzle

Think of a common nine-letter word that contains five consecutive consonants.
Take three consecutive consonants out of these five and replace them with vowels
to form another common nine-letter word. What is it?
This is part of solving the NPR Sunday Puzzle for Mar. 20, 2016

"""

import sys, logging


__author__ = 'rnzucker'

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

CONSONANTS ='bcdfghjklmnpqrstvwxyz'

def five_consec_consonants(word):
    """ Return True if there are five consecutive consonants in the word
    :param word: a nine letter word to check
    :return: True if there are five consecutive consonants
    """
    for i in range(5):
        if word[i] in CONSONANTS: # check to see if letter 0-4 are consonants is a consonant
            if (word[i+1] in CONSONANTS) and (word[i+2] in CONSONANTS) and (word[i+3] in CONSONANTS)\
                and (word[i+4] in CONSONANTS):
                return True
    return False


def main():
    # word_file = open("words.txt", "r")
    word_file = open("../03-06-16/long-wordsEn.txt", "r")
    out_file  = open("nine-out.txt", "w")
    words = word_file.readlines()
    num_words = len(words)
    print("There are {} words.\n".format(num_words))

    j = 0
    nine_words = []
    for i in range(num_words):
        num_chars = len(words[i])
        if num_chars==10: # Newline is included in the number of characters
            # Remove \n
            temp = words[i][0:9].rstrip()
            out_file.write(words[i])
            if five_consec_consonants(temp):
                # Append word to end
                nine_words.append(temp)
                print(nine_words[j])
                j = j + 1
    print("\n", j, "nine letter words with five consecutive consonants.\n")
    out_file.close()




# Check for interactive session
if __name__ == '__main__':
    # execute main program
    main()
