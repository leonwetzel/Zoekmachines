#!/usr/bin/python3

"""
Week 2
Search Engines / Zoekmachines
@author Leon F.A. Wetzel
University of Groningen / Rijksuniversiteit Groningen

l.f.a.wetzel@student.rug.nl
"""


def bigram(l1, l2):
    """
    Write a Python3 function bigram(l1,l2) which takes two sorted lists of positions as argument.
    The function returns "True" if there is a position p in the first list such that there is
    a position p+1 in the second list. In all other cases the function returns "False".
    Your solution should exploit the fact that both lists are ordered.
    """
    # This was an attempt to implement a less naive way of intersection...
    # it1 = iter(l1)
    # it2 = iter(l2)
    # sol = False
    #
    # n1 = next(it1)
    # n2 = next(it2)
    # while True:
    #     try:
    #         if n1 == n2 + 1:
    #             return True
    #         else:
    #             if n1 < n2:
    #                 n1 = next(it1)
    #             else:
    #                 n2 = next(it2)
    #     except StopIteration:
    #         return sol

    # Below is a naive way of intersection. However, it works...
    sol = False
    try:
        # naive implementation
        for p in l1:
            for j in l2:
                if p == j + 1:
                    sol = True
        print(sol)

    except TypeError:
        print(sol)


if __name__ == "__main__":
    bigram(l1=[], l2=[])
