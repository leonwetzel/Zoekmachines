#!/usr/bin/python3

"""
Week 6
Search Engines / Zoekmachines
@author Leon F.A. Wetzel
University of Groningen / Rijksuniversiteit Groningen
l.f.a.wetzel@student.rug.nl
"""
import sys
from collections import Counter


def main():
    """
    Define a Python function which computes the value of kappa for two given lists of judgements.
    Ensure your program can accept any judgement values (not just 0 or 1, but also a choice from,
    say, green, blue or red). Your program should read a file with judgements, and write out the 
    kappa value.
    """
    left = []
    right = []
    counter = 0
    total = 0

    for line in sys.stdin:
        try:
            [a, b] = line.rstrip().lower().split()
        except ValueError:
            [a, b] = line.rstrip().lower().split('\t')

        left.append(a)
        right.append(b)

        if a == b:
            counter += 1

        total += 1

    a = counter / total
    e = calculate_chance_agreement(left, right, total)

    print("{}".format(kappa(a, e)))


def calculate_chance_agreement(left, right, total):
    """
    Calculates chance agreement.
    :param: Values from left row
    :param: Values from right row
    :param: Total amount of cases
    :return: Rounded chance agreement
    """
    left_counts = dict(Counter(left))
    right_counts = dict(Counter(right))
    result = 0

    for i in left_counts:
        result += calculate_chance(left_counts[i], total) * calculate_chance(right_counts[i], total)

    return round(result, 4)


def kappa(a, e):
    """
    Calculates kappa value.
    kappa = fraction of agreement cases / fraction of chance agreement cases
    :return: Rounded kappa value
    """
    return round(float((a - e) / (1 - e)), 4)


def calculate_chance(judgements, cases):
    """
    Divide the amount of judgements by the total amount of cases
    :return: Chance
    """
    return float(judgements / cases)

if __name__ == "__main__":
    main()
