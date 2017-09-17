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
import re


def main():
    """
    We use the same Twitter data as last week. Write a Python3 program which builds a database
    where you record for each term in which tweet the term occurs, and in addition records the
    ordered position list for a term in a tweet. The database is saved with the pickle module.
    Hint: take into account the next exercise to come up with a good data structure.
    Hint: in Python, elements of a set must be immutable. This implies that certain otherwise
    reasonable choices must be avoided. 
    :return: 
    
    DB structure: term | tweetID | ordered position list for term in tweet
    """

    # at the end, the dictionary will be dumped to a pickle
    db = {}

    for line in sys.stdin:

        # reset values for every tweet
        positions = {}
        index = 0

        # split line in usable pieces and retrieve the tweet
        split = re.search('^(\d*)(\t{1})(\S+)(\t{1})(.+)(\t{1})(.+)$', line)

        # for each word
        for token in split.group(7).split():
            # if token already exists in the line
            if token in positions:
                # first we retrieve the current positions which the term holds in the line
                cur_pos = positions[token]
                # second, we add the current index to the temp list of positions
                cur_pos.append(index)
                # third, we insert the temp list into the positions
                positions.update({token: cur_pos})
                # fourth, we create a tuple which contains the tweet ID and the positions
                tup = (split.group(1), positions[token])
            else:
                # add token and index to positions
                item = {token: [index]}
                positions.update(item)

                # create tuple which contains tweet ID and current position
                tup = (split.group(1), [index])

            # fifth, we update the db dictionary
            db.update({token: tup})

            # increment index
            index += 1

    # build database
    with open('db.pickle', 'wb') as f:
        pickle.dump(db, f)
        sys.stderr.write("Data successfully dumped to db.pickle!\n")


if __name__ == "__main__":
    main()
