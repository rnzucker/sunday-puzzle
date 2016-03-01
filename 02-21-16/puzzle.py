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
        if num_chars==9: # Newline is included in the number of characters
            if ((words[i].find('g') != -1) or (words[i].find('G') != -1)):
                # Remove \n
                temp = words[i][0:8].rstrip()
                # Append word to end
                eight_words.append(temp)
                print(eight_words[j])
                j = j + 1
    print("\n", j, "eight letter words with a G\n")

    # Go through list of eight G words. If three words have the same first three letters,
    # create a new list of all words with those same first three letters. Starting from zero
    # up to n-2, search through remaining words for matches of fifth through eighth letters.
    # If next one in list doesn't match, move to next one in the outermost loop of this common
    # three letter prefix
    num_eight_gs = len(eight_words)
    i = 0
    while i < (num_eight_gs-2):
        if (eight_words[i][0:3] == eight_words[i+1][0:3]) and (eight_words[i][0:3] == eight_words[i+2][0:3]):
            # print(eight_words[i], eight_words[i+1], eight_words[i+2])
            three_same = []
            three_same.append(eight_words[i])
            three_same.append(eight_words[i+1])
            three_same.append(eight_words[i+2])
            j = 0
            # Loop through until you hit a different three starting letters. Start three beyond the
            # current value of i. Hence the i+3+j calculation
            while (i+3+j) < num_eight_gs and (eight_words[i][0:3] == eight_words[i+3+j][0:3]):
                three_same.append(eight_words[i+3+j])
                j += 1
            print("Three or more same", three_same)

            # three_same is a list of three or more words where the first three letters are the same.
            # Compare letters five to eight in the first word to the same letters in all the remaining
            # words. If you don't get three matches, then start with the second word and do this again.
            k = 0
            while k < (len(three_same)-2):
                m = 1
                end_match = 1
                rear_match = []
                rear_match.append(three_same[k])
                while k+m < len(three_same):
                    if three_same[k][4:8] == three_same[k+m][4:8]:
                        end_match += 1
                        rear_match.append(three_same[k+m])
                        # print("End match", end_match, rear_match)
                        if end_match >= 3:
                            print("REAR MATCH", rear_match)
                    m += 1
                k += 1
            i = i + 2 + j
            # if (eight_words[i][4:7] == eight_words[i+1][4:7]) and (eight_words[i][4:7] == eight_words[i+2][4:7]):
            #     print(eight_words[i], eight_words[i+1], eight_words[i+2])
        i += 1




# Check for interactive session
if __name__ == '__main__':
    # execute main program
    main()
