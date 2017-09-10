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

# Initiate a dictionary
dictionary = {}

# Use regular expressions to cut every line in usable pieces and
# insert those pieces - which form a tuple - into the dictionary
for line in fileinput.input():
    try:
        split = re.search('^(\d*)(\t{1})(\S+)(\t{1})(.+)(\t{1})(.+)$', line)

        # FOR TEST PURPOSES:
        # print(user + " -> " + text + " -> " + words)

        dictionary.update({split.group(1): (split.group(3), split.group(5), split.group(7))})

    except Exception as e:
        # Just in case ;)
        print(e)


# Saves dictionary as pickle
with open('tweets.pickle', 'wb') as f:
    pickle.dump(dictionary, f)
