#!/usr/bin/python3

'''
Week 1
Search Engines / Zoekmachines
@author Leon F.A. Wetzel
University of Groningen / Rijksuniversiteit Groningen

l.f.a.wetzel@student.rug.nl
'''

import pickle
import fileinput
import re
import string

# Initiate dictionaries and set
dictionary = {}
postings = set()
words = {}

# Use regular expressions to cut every line in usable pieces and
# only grab the words. These words will be put on separate lines.
for line in fileinput.input():
    # APPLE and apple should be the same, for instance ;)
    line = line.lower()
    try:
        split = re.search('^(\d*)(\t{1})(\S+)(\t{1})(.+)(\t{1})(.+)$', line)
        words = split.group(7)
        words = words.replace(" ", "\n")
        words = words.translate(None, string.punctuation)

        postings.update(words)

        dictionary.update({split.group(1): (split.group(3), split.group(5), split.group(7))})

    except Exception as e:
        # Just in case ;)
        print(e)

print(postings)

# Saves dictionary as pickle
with open('tweets.pickle', 'wb') as f:
    pickle.dump(dictionary, f)
