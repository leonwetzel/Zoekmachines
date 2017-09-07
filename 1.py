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
    split = re.search('^(\d*)(\t{1})(\S+)(\t{1})(.+)(\t{1})(.+)$', line)
    key = split.group(1)
    user = split.group(3)
    text = split.group(5)
    words = split.group(7)


# Saves dictionary as pickle
with open('docs.pickle', 'wb') as f:
    pickle.dump(dictionary, f)
