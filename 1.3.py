#!/usr/bin/python3

'''
Week 1
Search Engines / Zoekmachines
@author Leon F.A. Wetzel
University of Groningen / Rijksuniversiteit Groningen

l.f.a.wetzel@student.rug.nl
'''

import pickle
import re
import string

import sys

dictionary = {}
postings = {}

# Use regular expressions to cut every line in usable pieces and
# only grab the words.
for line in sys.stdin:
    # APPLE and apple should be the same, for instance ;)
    line = line.lower()
    try:
        split = re.search('^(\d*)(\t{1})(\S+)(\t{1})(.+)(\t{1})(.+)$', line)

        # Retrieve tweet identifier
        # - also known as key
        identifier = split.group(1)
        # print("\n\nID -> " + identifier)

        # Generate tokens and place them in set 'new'
        new = split.group(7).split() #.translate(None, string.punctuation).split()
        # print("NEW ->")
        # print(new)

        # Dictionary structure:
        # Key = word
        # Value = posting list (i.e. tweet identifier(s) in which the word occurs)

        # Example structure of dictionary:
        # example = {"the": {902078295159828480, 902078295499526144}}
        # - where example is a dictionary which will be inserted into dictionary postings

        # new = set of words in a tweet
        for token in new:
            # print("TOKEN -> " + token)
            if token in postings:
                # Update the set of identifiers of a certain token in the dictionary
                identifiers = postings[token]
                identifiers.add(identifier)
                postings.update({token: identifiers})

                # print("POSTING1 ->")
                # print(postings[token])
            else:
                # Insert a new token into the dictionary
                item = {token: {identifier}}
                postings.update(item)

                # print("POSTING2 ->")
                # print(postings[token])

        dictionary.update({split.group(1): (split.group(3), split.group(5), split.group(7))})

    except Exception as e:
        # Just in case ;)
        print(e)

# Saves posting list dictionary as pickle
with open('postinglist.pickle', 'wb') as p:
    pickle.dump(postings, p)
    # print("Posting list successfully dumped to pickle!", file=sys.stderr)
    sys.stderr.write("Posting list successfully dumped to pickle!\n")

# Saves tweets dictionary as pickle
with open('tweets.pickle', 'wb') as f:
    pickle.dump(dictionary, f)
    # print("Tweets successfully dumped to pickle!", file=sys.stderr)
    sys.stderr.write("Tweets successfully dumped to pickle!\n")
