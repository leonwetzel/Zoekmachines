#!/usr/bin/python3

"""
Week 3
Search Engines / Zoekmachines
@author Leon F.A. Wetzel
University of Groningen / Rijksuniversiteit Groningen

l.f.a.wetzel@student.rug.nl
"""
import sys
vowels = ['a', 'i', 'u', 'e', 'o']


def main():
    """
    Variant of Levenshtein. In order to make the exercise a bit more interesting,
    you will now implement a variant of Levenshtein distance. In this variant,
    insertion and deletion of a vowel only costs 0.5. Insertion and deletion of
    all other characters costs 1. Substitution has a cost of 1 as well, except if
    a vowel is substituted by a vowel which has a cost of 0.5. For the purpose of
    this exercise, vowels simply are characters a, e, i, o and u. Here are some
    examples: file kev.in. The following pipe should produce output that is
    identical to ew.out. 
    :return: 
    """

    for line in sys.stdin:
        # separate input and assign words to w1 and w2
        try:
            [w1, w2] = line.rstrip().split('\t')
        except ValueError:
            # just in case someone makes an input error
            sys.stderr.write("Cannot accept input. Please use TAB between the words!\n")
            sys.exit()

        # print both words and Levenshtein distance
        print("{}\t{}\t{}".format(w1, w2, custom_levenshtein(w1, w2)))


def custom_levenshtein(w1, w2):
    """
    A dynamic programming solution to find the custom Levenshtein distance
    for two words.
    :param w1: first word
    :param w2: second word
    :return: custom Levenshtein distance
    """

    # base checks
    if len(w1) < len(w2):
        # check if length of word1 is smaller than word2.
        # if so, call function and switch parameters
        return custom_levenshtein(w2, w1)
    elif len(w1) == 0:
        # if the length of word1 equals 0, that means that
        # the Lev' distance is the length of word2
        return len(w2)
    elif len(w2) == 0:
        # if the length of word2 equals 0, that means that
        # the Lev' distance is the length of word1
        return len(w1)
    elif w1 == w2:
        # check if words are simply the same
        return 0

    # we use this information to determine the range of 'previous' and the
    # matrix in general
    previous = range(len(w2) + 1)

    # DEBUG
    # print("PREV -> \t" + str(previous))

    # iterate over the characters of the first word
    for a, char1 in enumerate(w1):
        # DEBUG
        # print("\na -> \t" + str(a))
        # print("\tchar1 -> \t" + str(char1))

        # the matrix-in-development
        # see bloed/bode example from sheets w3
        # matrix = [a + 1]
        matrix = [a]

        # iterate over the characters of the second word
        for b, char2 in enumerate(w2):
            # DEBUG
            # print("b -> \t" + str(b))
            # print("\tchar2 -> \t" + str(char2))

            # in order to improve readability of the code,
            # I decided to split if-statements and 'copy'
            # the code across several statements.
            if (char1 in vowels and char2 in vowels) and a == b:
                inserts = previous[b + 1] + 0.5
                deletions = matrix[b] + 0.5
                subs = previous[b] + (char1 != char2)/2
            elif char1 in vowels and (a > b or a < b):
                inserts = previous[b + 1] + 0.5
                deletions = matrix[b] + 0.5
                subs = previous[b] + (char1 != char2)/2
            else:
                inserts = previous[b + 1] + 1
                deletions = matrix[b] + 1
                subs = previous[b] + (char1 != char2)

            # DEBUG
            # print("char1 != char2 -> \t" + str(char1 != char2))
            # print("INSERTS -> \t" + str(inserts))
            # print("DELS -> \t" + str(deletions))
            # print("SUBS -> \t" + str(subs))

            # add the minimum to the matrix
            matrix.append(min(inserts, deletions, subs))

            # DEBUG
            # print("CURRENT -> \t" + str(matrix))
        previous = matrix

    # print(str(previous[-1]))
    return float(previous[-1])

if __name__ == "__main__":
    main()
