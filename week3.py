#!/usr/bin/python3

"""
Week 3
Search Engines / Zoekmachines
@author Leon F.A. Wetzel
University of Groningen / Rijksuniversiteit Groningen

l.f.a.wetzel@student.rug.nl
"""
import sys
distance = int


def main():
    """
    Variant of Levenshtein. In order to make the exercise a bit more interesting,
    you will now implement a variant of Levenshtein distance. In this variant,
    insertion and deletion of a vowel only costs 0.5. Insertion and deletion of
    all other characters costs 1. Substitution has a cost of 1 as well, except if
    a vowel is substituted by a vowel which has a cost of 0.5. For the purpose of
    this exercise, vowels simply are characters a, e, i, o and u. Here are some
    examples: file lev_vowel.in. The following pipe should produce output that is
    identical to lev_vowel.out. 
    :return: 
    """

    for line in sys.stdin:
        # reset distance to 0
        distance = 0
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
    A dynamic programming solution to find the alternative Levenshtein distance
    for two words.
    :param w1: first word
    :param w2: second word
    :return: Levenshtein distance
    """

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

    # thanks to the check above, we can assume that w2 is the longest word
    # we use this information to determine the range of 'previous'
    previous = range(len(w2) + 1)

    # DEBUG
    # print(previous)

    # iterate over the characters of the first word
    for a, char1 in enumerate(w1):
        # DEBUG
        # print("i -> " + str(a))
        # print("char1 -> " + str(char1))

        current = [a + 1]

        # iterate over the characters of the second word
        for b, char2 in enumerate(w2):
            # DEBUG
            # print("j -> " + str(b))
            # print("\tchar2 -> " + str(char2))

            inserts = previous[b + 1] + 1
            deletions = current[b] + 1
            subs = previous[b] + (char1 != char2)

            # DEBUG
            # print(str(char1 != char2))
            # print("INSERTS -> " + str(inserts))
            # print("DELS -> " + str(deletions))
            # print("SUBS -> " + str(subs))

            current.append(min(inserts, deletions, subs))

            # DEBUG
            # print("CURRENT -> " + str(current))
        previous = current

    return previous[-1]

if __name__ == "__main__":
    main()
