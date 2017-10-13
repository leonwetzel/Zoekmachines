#!/usr/bin/python3

"""
Week 6
Search Engines / Zoekmachines
@author Leon F.A. Wetzel
University of Groningen / Rijksuniversiteit Groningen
l.f.a.wetzel@student.rug.nl
"""

import sys

for line in sys.stdin:
  [a, b] = line.rstrip().split('\t')
  print(a)
  print(b)
  
