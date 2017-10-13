#!/usr/bin/python3

"""
Week 6
Search Engines / Zoekmachines
@author Leon F.A. Wetzel
University of Groningen / Rijksuniversiteit Groningen
l.f.a.wetzel@student.rug.nl
"""

import sys

def main():
  """
  Define a Python function which computes the value of kappa for two given lists of judgements.
  Ensure your program can accept any judgement values (not just 0 or 1, but also a choice from,
  say, green, blue or red). Your program should read a file with judgements, and write out the 
  kappa value.
  """
  for line in sys.stdin:
    [a, b] = line.rstrip().split('\t')
    print(a)
    print(b)
  
if __name__ == "__main__":
    main()
