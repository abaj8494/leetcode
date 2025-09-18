# @leet imports start
from string import *
from re import *
from datetime import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
from random import *
from statistics import *
from itertools import *
from functools import *
from operator import *
from io import *
from sys import *
from json import *
from builtins import *
import string
import re
import datetime
import collections
import heapq
import bisect
import copy
import math
import random
import statistics
import itertools
import functools
import operator
import io
import sys
import json
from typing import *
# @leet imports end

# @leet start
import itertools
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        positions = set()
        perms = [''.join(q) for q in itertools.permutations(p)]

        for perm in perms:
            for i in range(len(s)):
                index = s.find(perm, i)
                if index == -1:
                    continue
                if index not in positions:
                    positions.add(index)
                i = index + 1
        return list(positions)
        """
        if len(p) > len(s): return []
        pCount, sCount = {}, {}
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i],0)
            sCount[s[i]] = 1 + sCount.get(s[i],0)

        res = [0] if sCount == pCount else []
        l = 0

        for r in range(len(p), len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r],0)
            sCount[s[l]] -= 1

            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l+=1
            if sCount == pCount:
                res.append(l)
        return res


        
# @leet end
