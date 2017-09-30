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
        dict(tweetID : (username, tweet, words))
        
    STRUCTURE FOR postinglist.pickle
        dict(term : [tweetID's])
    
    :return: 
    """
    for line in sys.stdin:
        # retrieve terms
        [q1, q2] = line.rstrip().lower().split()

        if q1 not in postings:
            replace_by_lev(q1)
        if q2 not in postings:
            replace_by_lev(q2)

        print(q1)
        print(q2)

        # sys.stderr.write("Terms not in posting lists.\n")

        # below is the ideal situation!

        p1 = set(postings[q1])
        p2 = set(postings[q2])

        # set with ID's of tweets in which both terms occur
        intersection = p1 & p2

        # print(intersection)

        for tweet in intersection:
            if (q1, tweet) in db and (q2, tweet) in db:
                if bigram(db[(q1, tweet)], db[(q2, tweet)]):
                    print_tweet(tweet)
            else:
                sys.stderr.write("No results found.\n")


def replace_by_lev(word):
    """
    Replaces a 'wrong' word with another word from the postinglist.
    The postingslist contains every indexed word from the tweets database.
    :param word: 
    :return: 
    """
    minimum = 0
    for term in postings:
        if levenshtein(word, term) > minimum:
            minimum = levenshtein(word, term)
            word = term
    return word


def levenshtein(w1, w2):
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
        return levenshtein(w2, w1)
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


def jaccard(set1, set2):
    """
    Calculates Jaccard index.
    :param set1: 
    :param set2: 
    :return: 
    """
    n = len(set1.intersection(set2))
    return n / float(len(set1) + len(set2) - n)


def print_tweet(tweet_id):
    """
    Prints tweet based on given tweet ID.
    :param tweet_id: ID of tweet
    """
    try:
        print(tweets[tweet_id][2])
    except TypeError:
        sys.stderr.write("Not a valid tweet ID.")


def ngrams(input, n):
    """
    Generates n-grams, based on input string.
    :param input: 
    :param n: 
    :return: n-grams
    """
    input = list(input)
    output = []
    for i in range(len(input) - n + 1):
        output.append(input[i:i + n])
    return output


def bigram(poslist1, poslist2):
    it1 = iter(poslist1)
    it2 = iter(poslist2)
    n1 = next(it1)
    n2 = next(it2)

    while True:
        try:
            if n1 == n2 - 1:
                return True
            else:
                if n1 < n2 - 1:
                    n1 = next(it1)
                else:
                    n2 = next(it2)
        except StopIteration:
            return False


if __name__ == "__main__":
    main()
