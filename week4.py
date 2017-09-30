#!/usr/bin/python3

"""
Week 3
Search Engines / Zoekmachines
@author Leon F.A. Wetzel
University of Groningen / Rijksuniversiteit Groningen

l.f.a.wetzel@student.rug.nl
"""
import sys
import pickle

db = pickle.load(open('db.pickle', 'rb'), encoding="utf-8")
tweets = pickle.load(open('tweets.pickle', 'rb'), encoding="utf-8")
postings = pickle.load(open('postinglist.pickle', 'rb'), encoding="utf-8")


def main():
    """
    Twitter Search with spell correction. On the basis of programming exercise 4 of week 1.
    Adapt the Twitter query system as follows. If there are no hits for the given query term,
    adapt the query so that it uses a query term that is very close to the original query term
    (e.g, a query term which does have hits and which is closest in terms of Levenshtein distance).
    NB. Use the standard version of Levenshtein distance for this exercise (without the alternative
    score for vowels).
    
    STRUCTURE FOR db.pickle
        DB structure: term | tweetID | ordered position list for term in tweet
        dict(tup(term, tweet ID) : [positions])
        So, dict key = (term, tweet ID)
        
    STRUCTURE FOR tweets.pickle
        tweetdID    username    tweet   words
        dict(tweetID : (username, tweet, words))
    
    :return: 
    """
    for line in sys.stdin:

        [q1, q2] = line.rstrip().split()


def lev(w1, w2):
    """
    A dynamic programming solution to find the Levenshtein distance of two words.
    Based on implementation from week 3.
    :param w1: first word
    :param w2: second word
    :return: Levenshtein distance
    """

    if len(w1) < len(w2):
        # check if length of word1 is smaller than word2.
        # if so, call function and switch parameters
        return lev(w2, w1)
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

    # iterate over the characters of the first word
    for a, char1 in enumerate(w1):
        current = [a + 1]
        # iterate over the characters of the second word
        for b, char2 in enumerate(w2):
            inserts = previous[b + 1] + 1
            deletions = current[b] + 1
            subs = previous[b] + (char1 != char2)
            current.append(min(inserts, deletions, subs))
        previous = current

    return previous[-1]

if __name__ == "__main__":
    main()
