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

db = pickle.load(open('db.pickle', 'rb'))
tweets = pickle.load(open('tweets.pickle', 'rb'))
postings = pickle.load(open('postinglist.pickle', 'rb'))


def main():
    """
    Based on the previous exercise, build a program which loads the database and
    then takes queries from standard input. Each query contains two terms (separated by space),
    q1 and q2. Your program returns all tweets where q1 directly precedes q2. 
    :return: 
    
    DB structure: term | tweetID | ordered position list for term in tweet
    dict(term, tup(tweet ID, [positions]))
    """

    for line in sys.stdin:
        # retrieve the terms from stdin
        # echo "de man"
        [q1, q2] = line.rstrip().split()

        # bind terms
        term1 = db[q1]
        term2 = db[q2]



        # check if keys both are in the big posting list.
        # this way, we limit the search to tweets which at least contain both terms
        if q1 in postings and q2 in postings:
            for identifier in postings[q1] & postings[q2]:
                # retrieve db record

                print(identifier)


if __name__ == "__main__":
    main()
