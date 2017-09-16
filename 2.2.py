#!/usr/bin/python3

"""
Week 2
Search Engines / Zoekmachines
@author Leon F.A. Wetzel
University of Groningen / Rijksuniversiteit Groningen

l.f.a.wetzel@student.rug.nl
"""

import sys
import pickle
import re

tweets = pickle.load(open('tweets.pickle', 'rb'))


def main():
    """
    Write a Python3 program which reads tweets from standard input (same format as last week).
    Your program prints for each tweet for each word the sorted position list of that word in that tweet.
    :return: 
    """
    # for each tweet (assuming that every line consists of ONE tweet ;))
    for line in sys.stdin:

        # reset values for every tweet
        positions = {}
        index = 0

        # split line in usable pieces and retrieve the tweet
        split = re.search('^(\d*)(\t{1})(\S+)(\t{1})(.+)(\t{1})(.+)$', line)

        # for each word
        for token in split.group(7).split():
            # if word is already index, add current position to positions
            if token in positions:
                cur_pos = positions[token]
                cur_pos.add(index)
                positions.update({token: cur_pos})
                # print('{}\t{}'.format(token, positions[token]))
            else:
                item = {token: {index}}
                positions.update(item)

                # print('{}\t{}'.format(token, positions[token]))
            # increment index
            index += 1

        for word in positions:
            print('{}\t{}'.format(word, positions[word]))

if __name__ == "__main__":
    main()
