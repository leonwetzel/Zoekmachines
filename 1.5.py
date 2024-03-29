#!/usr/bin/python3

'''
Week 1
Search Engines / Zoekmachines
@author Leon F.A. Wetzel
University of Groningen / Rijksuniversiteit Groningen

l.f.a.wetzel@student.rug.nl
'''

import pickle
import sys

# Load pickles
tweets = pickle.load(open('tweets.pickle', 'rb'), encoding="utf-8")
postings = pickle.load(open('postinglist.pickle', 'rb'), encoding="utf-8")

for key in sys.stdin:
    # Get two keys/words from stdin.
    # Courtesy of stdin sending two keys, of course.
    [firstKey, secondKey] = key.rstrip().split()

    # Check if keys both are in the big posting list.
    if firstKey in postings and secondKey in postings:
        # Find the identifier of the tweet in which the two keys match.
        # If found, print the tweet and repeat the process until there
        # are no more matches to be found.
        for identifier in postings[firstKey] & postings[secondKey]:
            print("Tweet:\t" + tweets[identifier][2])

