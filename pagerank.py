#!/usr/bin/python3

"""
Week 7
Search Engines / Zoekmachines
@author Leon F.A. Wetzel
University of Groningen / Rijksuniversiteit Groningen
l.f.a.wetzel@student.rug.nl
"""
import sys
import numpy


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
        try:
            matrix.append([float(x) for x in line.rstrip().split('\t')])
        except ValueError:
            matrix.append([float(x) for x in line.rstrip().split()])

    standard_vector = generate_standard_vector(matrix)
    pr = pagerank(standard_vector, matrix)
    print(*pr, sep="\t")


def pagerank(standard, matrix):
    """
    Calculates pagerank, based on a standard vector and a given matrix.
    
    :param standard: 
    :param matrix: 
    :return: 
    """
    new = []
    mat = []

    while new != standard:
        if new:
            standard = new.copy()
            new.clear()
            mat.clear()

        for i, row in enumerate(matrix):
            rij = []
            for j, item in enumerate(row):
                rij.append(item * standard[i])
            mat.append(rij)

        for i, row in enumerate(mat):
            new.append(round(sum([item[i] for item in mat]), 4))

    return new


def generate_standard_vector(matrix):
    """
    Generates a standard vector based on given matrix length.
    :param matrix: 
    :return: 
    """
    vector = []
    for item in matrix:
        vector.append(1/len(matrix))
    vector = fix_stochastic(vector)
    return vector


def fix_stochastic(vector):
    """
    Make sure that vector is right stochastic.
    Applies correction if vector is not right stochastic.
    :param vector: 
    :return: (fixed) vector
    """
    if sum(vector) != 1:
        vector.pop()
        fix = 1 - sum(vector)
        vector.append(fix)
    return vector

if __name__ == "__main__":
    main()
