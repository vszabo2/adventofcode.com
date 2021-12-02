#!/usr/bin/env python3.10
from itertools import pairwise as p
print(sum(a<b for a,b in p(map(int,open('input')))))
