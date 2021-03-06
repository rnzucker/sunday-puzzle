"""Playing around with Python to do the Sunday Puzzle

Sunday puzzle from Mar, 6, 2016:
Bail, Nail, and Mail are three four-letter words that differ only by their first
letters. And those first letters (B, N, and M) happen to be adjacent on a computer
keyboard. Can you think of five four-letter words that have the same property —
that is, they're identical except for their first letters, with those first letters
being adjacent on the keyboard? All five words must be ones that everyone knows.
Capitalized words and plurals are not allowed. What words are they?

Part of solution involves scanning words file for 4-letter words and creating
a new list with the words, but with the letter order reversed. Also, when the words
are put back in regular order, need to sort by the order of the keys on the keyboard,
so a special key function is needed.

"""

import sys, logging


__author__ = 'rnzucker'

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

ROW1 = 'qwertyuiop'  # Letters, in order, in first row of keyboard
ROW2 = 'asdfghjkl'   # Letters, in order, in second row of keyboard
ROW3 = 'zxcvbnm'     # Letters, in order, in third row of keyboard


def row_in_order(sorted_words):
    """ Check to see if the first five words have first letters that are adjacent in row

    :rtype : Boolean
    :param sorted_words: array of five four letter words, all of whose first letters appear in the same row as
                         the row passed in in the row parameter, and whose last three letters are the same.
                          The words are ordered based upon the order of letters in that keyboard row.
    :return: True if the first letter of the five words are adjacent on the keyboard
    """
    # Set row to the proper row
    if sorted_words[0][0] in ROW1:
        row = ROW1
    elif sorted_words[0][0] in ROW2:
        row = ROW2
    else: # Must be in ROW3. Not handling error case
        row = ROW3
    loc = row.find(sorted_words[0][0])
    if (sorted_words[1][0] == row[loc + 1]) and (sorted_words[2][0] == row[loc + 2]) and (
        sorted_words[3][0] == row[loc + 3]) and (sorted_words[4][0] == row[loc + 4]):
        return True
    return False

def row_key(letters):
    """ Used for sorting according to appropriate row order. Returns index of letter's location

    :param letters: word whose first letter is being checked
    :return: index in corresponding row
    """
    if letters[0] in ROW1:
        return ROW1.find(letters[0])
    elif letters[0] in ROW2:
        return ROW2.find(letters[0])
    else: # Must be in ROW3. Not handling error case.
        return ROW3.find(letters[0])


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

    # Create a two dimensional array, four_chars, of all four letter words. The first dimension is indexed by the
    # keyboard row of each word's first letter. The words are put into the array in reverse order, since we will
    # be looking for five words where the last three letters are the same.
    num_four = 0
    four_chars = [[],[],[]]
    for i in range(num_words):
        num_chars = len(words[i])
        if (num_chars == 5): # Newline is included in the number of characters
            # Remove \n
            temp = words[i][0:4].rstrip()
            # Append reverse form of word to end
            if temp[0] in ROW1:
                four_chars[0].append(temp[::-1])
            elif temp[0] in ROW2:
                four_chars[1].append(temp[::-1])
            elif temp[0] in ROW3:
                four_chars[2].append(temp[::-1])
            else:
                print(temp, "starts with non-letter")
            num_four += 1
    print("\n", num_four, "four letter words\n")
    # Sort by reversed words, so easier to find matches
    four_chars[0].sort()
    four_chars[1].sort()
    four_chars[2].sort()

    # Check first three letters (in reversed form) of five consecutive words to see if they match.
    # We know that the fourth letter are all in the same row of the keyboard since we have a separate
    # sub-array for each ROW.
    for i in range(3):
        len_row = len(four_chars[i])
        for j in range(len_row-4):
            # Five consecutive words with same last three letters (words are reversed)
            if (four_chars[i][j][0:3] == four_chars[i][j+1][0:3]) and (four_chars[i][j][0:3] == four_chars[i][j+2][0:3]) and\
                    (four_chars[i][j][0:3] == four_chars[i][j+3][0:3]) and (four_chars[i][j][0:3] == four_chars[i][j+4][0:3]):
                # Fill element array of words properly ordered. There can be more than five, so do it dynamically
                possible_words = []
                k = 0
                while (j+k < len_row) and (four_chars[i][j][0:3] == four_chars[i][j+k][0:3]):
                    possible_words.append(four_chars[i][j+k][::-1])
                    k += 1
                possible_words.sort(key=row_key)
                # We are only interested in the first five words, so we only check those
                if row_in_order(possible_words[0:5]):
                    print(possible_words[0:5])



# Check for interactive session
if __name__ == '__main__':
    # execute main program
    main()
