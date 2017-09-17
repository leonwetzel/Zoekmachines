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

# load pickles
db = pickle.load(open('db.pickle', 'rb'))
tweets = pickle.load(open('tweets.pickle', 'rb'), encoding="utf-8")


def main():
    """
    Based on the previous exercise, build a program which loads the database and
    then takes queries from standard input. Each query contains two terms (separated by space),
    q1 and q2. Your program returns all tweets where q1 directly precedes q2. 
    :return: 
    
    DB structure: term | tweetID | ordered position list for term in tweet
    dict(tup(term, tweet ID) : [positions])
    
    So, dict key = (term, tweet ID)
    """

    for line in sys.stdin:
        # retrieve the terms from stdin
        # EXAMPLE: echo "Ik zit"
        [q1, q2] = line.rstrip().split()

        for key in tweets:
            if (q1, key) in db and (q2, key) in db:
                pos1 = db[(q1, key)]
                pos2 = db[(q2, key)]

                # FIXME:
                # below is 'better' intersection algorithm
                # it slightly works, but I cannot find the proper solution...
                # it1 = iter(pos1)
                # it2 = iter(pos2)
                #
                # n1 = next(it1)
                # n2 = next(it2)
                # while True:
                #     try:
                #         if n2 == n1 + 1:
                #             print(tweets[key][2])
                #             n1 = next(it1)
                #             n2 = next(it2)
                #         else:
                #             if n1 < n2:
                #                 n1 = next(it1)
                #                 n2 = next(it2)
                #             else:
                #                 n1 = next(it1)
                #                 n2 = next(it2)
                #     except StopIteration:
                #         return 0

                # print("POS1 -> " + str(pos1))
                # print("POS2 -> " + str(pos2))

                # below is a naive implementation
                # we need to find a better intersection algorithm...
                for i in pos1:
                    # print("i -> " + str(i))
                    for j in pos2:
                        # print("j -> " + str(j))
                        if j == i + 1:
                            print("{}".format(tweets[key][2]))

if __name__ == "__main__":
    main()
