#!/usr/bin/python3

"""
Week 2
Search Engines / Zoekmachines
@author Leon F.A. Wetzel
University of Groningen / Rijksuniversiteit Groningen

l.f.a.wetzel@student.rug.nl
"""
import sys


def bigram(l1, l2):
    """
    Write a Python3 function bigram(l1,l2) which takes two sorted lists of positions as argument.
    The function returns "True" if there is a position p in the first list such that there is
    a position p+1 in the second list. In all other cases the function returns "False".
    Your solution should exploit the fact that both lists are ordered.
    """
    try:
        for line in sys.stdin:
            # check if lengths of lists are equal
            # if not equal, return false
            if len(l1) != len(l2):
                return False

            for p in l1:
                for j in l2:
                    if j == p + 1:
                        return True
            return False

    except TypeError:
        sys.stderr.write("Missing lists!")
        return False


if __name__ == "__main__":
    import sys
    bigram()
