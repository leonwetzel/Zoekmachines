Week 4
Zoekmachines / Search Engines
Rijksuniversiteit Groningen / University of Groningen

Leon F.A. Wetzel
s3284174
l.f.a.wetzel@student.rug.nl

TWITTER SEARCH WITH SPELL CORRECTION
------------------------------------

This program allows the user to search for a term in the tweets database. The program makes use of
pre-build posting lists, a database containing terms within a tweets and registered positions, and
a dictionary containg tweets, tweet ID's, author's and words of tweets.

Several techniques were used to execute the queries. Firstly, we search for the query term in the postings list.
This gives us a list containing the ID's of all the tweets in which the query term occurs.
In case the word cannot be found in the postings list, we compare the given query term with all other terms in the
postings lists by looking at the minimal Levenshtein distance of found word.

The user can select if they want to see results with all relevant terms or just the results of the term with the
highest amount of hits. This can be toggled by giving the '-a' of '--all' argument in the command line.

It is also possible to toggle the use of the Jaccard distance. Only if the Jaccard distance of two sets is maximal,
then the Levenshtein distance will be calculated.

How do you search?
...$ echo "jaar" | python3 week4.py

How do you search, whilst keeping the Jaccard distance in mind?
...$ echo "jaor" | python3 week.py -j

...$ echo "jaor" | python3 week.py --jaccard

How do you search and perform an OR-query in case multiple terms share the same minimal Levenshtein distance?
...$ echo "murkt" | python3 week4.py -a

...$ echo "jaor" | python3 week4.py --all

Combination of arguments
...$ echo "murkt" | python3 week.py -a -j

Questions and/or remarks? Do not hesitate to email me (l.f.a.wetzel@student.rug.nl)!
