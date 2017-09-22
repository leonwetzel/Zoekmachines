#!/usr/bin/python3

"""
Week 3
Search Engines / Zoekmachines
@author Leon F.A. Wetzel
University of Groningen / Rijksuniversiteit Groningen

l.f.a.wetzel@student.rug.nl
"""
import sys


def main():
    for line in sys.stdin:
        [w1, w2] = line.rstrip().split('\t')
        print(w1)
        print(w2)

if __name__ == "__main__":
    main()
