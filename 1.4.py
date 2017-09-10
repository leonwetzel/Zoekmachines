#!/usr/bin/python3

'''
Week 1
Search Engines / Zoekmachines
@author Leon F.A. Wetzel
University of Groningen / Rijksuniversiteit Groningen

l.f.a.wetzel@student.rug.nl
'''

import pickle

# Read from pickle's
tweets = pickle.load(open('tweets.pickle', 'rb'))
postings = pickle.load(open('postinglist.pickle', 'rb'))

# Display the tweets in which the word - a.k.a. key - can be found
for key in postings.keys():
    print("------------------")
    print("Word: " + key)
    for identifier in postings[key]:
        print("Tweet: " + tweets[identifier][1])
