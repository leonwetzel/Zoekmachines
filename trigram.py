#!/usr/bin/python3

"""
Week 4
Search Engines / Zoekmachines
@author Leon F.A. Wetzel
University of Groningen / Rijksuniversiteit Groningen

l.f.a.wetzel@student.rug.nl
"""
import sys
import pickle

postings = pickle.load(open('postinglist.pickle', 'rb'), encoding="utf-8")


def main():
    for line in postings:
        print(ngrams(line))


def ngrams(word, n=3):
    """
    Generates n-grams, based on a given word.
    :param word: 
    :param n: 
    :return: n-grams
    """
    word = list(word)
    word.insert(0, '$')
    word.append('$')

    output = []
    for i in range(len(word) - n + 1):
        output.append(word[i:i + n])
    return str(output)


if __name__ == "__main__":
    main()
