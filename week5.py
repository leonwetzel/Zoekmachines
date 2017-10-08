#!/usr/bin/python3

"""
Week 5
Search Engines / Zoekmachines
@author Leon F.A. Wetzel
University of Groningen / Rijksuniversiteit Groningen

l.f.a.wetzel@student.rug.nl
"""
import sys
import pickle
from operator import itemgetter
import math

VOWELS = ['a', 'i', 'u', 'e', 'o']

db = pickle.load(open('db.pickle', 'rb'), encoding="utf-8")
tweets = pickle.load(open('tweets.pickle', 'rb'), encoding="utf-8")
postings = pickle.load(open('postinglist.pickle', 'rb'), encoding="utf-8")

TWEET_AMOUNT = len(tweets)


def main():
    """
    Programming exercise: take the Twitter-search-engine from the last few weeks
    as a starting point. Implement a variant which takes two search terms and then
    returns all tweets which match at least one of the search terms. Add the tf-idf
    score of each document. Order the returned documents by tf-idf score.

    creation of data-structure:
    you need to maintain, for each term, in how many documents that term occurs.
    It is ok to use the length of the posting list for this purpose.
    you also need to maintain the overall number of tweets
    you need to maintain how often a word occurs in a tweet 
    
    STRUCTURE FOR db.pickle
        DB structure: term | tweetID | ordered position list for term in tweet
        dict(tup(term, tweet ID) : [positions])
        So, dict key = (term, tweet ID)
        
    STRUCTURE FOR tweets.pickle
        dict(tweetID : (username, tweet, words))
        
    STRUCTURE FOR postinglist.pickle
        dict(term : [tweetID's])
        
    NOTICE: this program also contains code for using this program with two terms!
    
    :return: 
    """

    for line in sys.stdin:
        # retrieve term(s)
        [q1, q2] = line.rstrip().lower().split()

        if q1 not in postings:
            w1 = sorted(replace_by_lev(q1).items(), key=itemgetter(1))
            w1 = w1[len(w1)-1][0]
            print("w1 => " + str(w1))
        else:
            w1 = q1

        if q2 not in postings:
            w2 = sorted(replace_by_lev(q2).items(), key=itemgetter(1))
            w2 = w2[len(w2)-1][0]
            print("w2 => " + str(w2))
        else:
            w2 = q2

        p1 = set(postings[w1])
        p2 = set(postings[w2])
        # intersection contains ID's of tweets in which w1 or w2 or both w1 and w2 occur.
        intersection = p1 | p2

        results = {}
        for tweet_id in intersection:
            if (w1, tweet_id) in db and (w2, tweet_id) in db:
                # if bigram(db[(w1, tweet)], db[(w2, tweet)]):
                score = normalize_vector(tf_idf(w1, tweet_id), tf_idf(w2, tweet_id))
                results.update({tweet_id: score})
            elif (w1, tweet_id) in db:
                score = normalize_vector(tf_idf(w1, tweet_id))
                results.update({tweet_id: score})
            elif (w2, tweet_id) in db:
                score = normalize_vector(tf_idf(w2, tweet_id))
                results.update({tweet_id: score})

        for identifier, score in reversed(sorted(results.items(), key=itemgetter(1))):
            print(score)
            print_tweet(identifier)


def tf_idf(term, document):
    """
    Calculates TF-IDF score for a term in a document.
    TF-IDF = TF * IDF
    - term frequency * inverted document frequency
    :return: 
    """
    return tf(term, document) * math.log(TWEET_AMOUNT / df(term))


def tf(term, document):
    """
    Calculates term frequency of term in document.
    :param term: a word
    :param document: a tweet
    :return: term frequency
    """
    return len(db[(term, document)])


def df(term):
    """
    Calculates document frequency of term.
    (in how many documents does term occur?)
    :param term: 
    :return: 
    """
    return len(postings[term])


def normalize_vector(score1, score2=None):
    """
    Normalizes vector by dividing each cell in the vector by its length.
    :param score1: first element
    :param score2: second element (optional)
    :return: 
    """
    if score2 is None:
        return score1 / math.sqrt(score1 ** 2)
    else:
        return (score1 + score2) / (math.sqrt(score1**2 + score2**2))


def build_alternatives(replacements):
    """
    Builds a list containing alternative search terms.
    :param replacements: 
    :return: 
    """
    alternatives = []
    highest = 0
    prev_lev = 0

    for term in replacements:
        # print("\nterm => " + str(term))
        lev = term[1][0]
        hits = term[1][1]

        if lev < 2 or lev == prev_lev:
            if hits > highest:
                highest = hits
                # print("\nterm => " + str(term))
                alternatives.append(term[0])
                prev_lev = lev

    return alternatives


def replace_vowels(word):
    """
    Generates a list of variant words of a given word.
    The variants contain different vowels.
    :param word: 
    :return: list of variant words
    """
    variants = []
    for c in word:
        if c in VOWELS:
            for vowel in VOWELS:
                variants.append(word.replace(c, vowel))
    return variants


def replace_by_lev(word):
    """
    Replaces a 'wrong' word with another word from the postinglist.
    The postingslist contains every indexed word from the tweets database.
    
    dict(term: tup(mininum_lev, occurrences))
    
    :param word: 
    :return: 
    """
    minimum_lev = -1
    results = {}

    it = iter(postings)
    term = next(it)

    while True:
        try:
            lev = levenshtein(word, term)
            postings_length = len(postings[term])
            if lev <= 1:  # and (postings_length >= hits):
                # print("MIN => " + str(minimum_lev))
                minimum_lev = lev
                results.update({term: (minimum_lev, postings_length)})
                term = next(it)
            else:
                if lev < minimum_lev:
                    minimum_lev = lev
                    results.update({term: (minimum_lev, postings_length)})
                term = next(it)
        except StopIteration:
            print(results)
            return results


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


def print_tweet(tweet_id):
    """
    Prints tweet based on given tweet ID.
    :param tweet_id: ID of tweet
    """
    try:
        print(tweets[tweet_id][2] + '\n')
    except TypeError:
        sys.stderr.write("Not a valid tweet ID.\n")


def ngrams(word, n):
    """
    Generates n-grams, based on a given word.
    :param word: 
    :param n: 
    :return: n-grams
    """
    word = list(word)
    # insert extra tokens
    word.insert(0, '$')
    word.append('$')

    output = []
    for i in range(len(word) - n + 1):
        # print(i)
        # print(word[i:i + n])
        output.append(''.join(word[i:i + n]))
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
