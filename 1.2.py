#!/usr/bin/python3

'''
Week 1
Search Engines / Zoekmachines
@author Leon F.A. Wetzel
University of Groningen / Rijksuniversiteit Groningen

l.f.a.wetzel@student.rug.nl
'''

import pickle

# Read from pickle
tweets = pickle.load(open('tweets.pickle', 'rb'))

# Display the words [2] for every tweet in the pickle
for key in tweets:
    print(tweets[key][2])
