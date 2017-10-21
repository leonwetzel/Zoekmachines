#!/usr/bin/python3

"""
Week 7
Search Engines / Zoekmachines
@author Leon F.A. Wetzel
University of Groningen / Rijksuniversiteit Groningen
l.f.a.wetzel@student.rug.nl
"""

import sys


def main():
    """
    Write a Python program which computes the PageRank vector for a given probability matrix P.
    The program computes the vectors x_1, x_2, x_3, ... until no further changes happen. The
    program prints all intermediate vectors. Your program should assume that the input probability
    matrix already represents the probability of teleports. Your program reads the probablity matrix
    from standard input. The matrix is provided in a simple text format where each row is a line,
    which consists of each of the values separated by TAB.
    :return: 
    """
    matrix = []
    for line in sys.stdin:
        matrix.append([str(x) for x in line.rstrip().split('\t')])
    print(matrix)

if __name__ == "__main__":
    main()
