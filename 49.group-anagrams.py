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
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        #O(mnlogn) sorting bruteforce
        print(strs)
        base = []
        for string in strs:
            base.append("".join((sorted(string))))

        print(base)
        # find indices that are all the same
        idxs = []
        marked = []
        for i, word1 in enumerate(base):
            i_likes = []
            for j, word2 in enumerate(base):
                if word1 == word2 and i <= j and j not in marked:
                    marked.append(j)
                    i_likes.append(j)
            if i_likes:
                idxs.append(i_likes)


        print(idxs)
        # replace indices with words:
        ans = []
        for tup in idxs:
            sublist = []
            for idx in tup:
                sublist.append(strs[idx])
            ans.append(sublist)

        return ans
        """

        # hashmap: O(m*n)
        hash = {}
        for s in strs:

            count = [0] * 26
            for c in s:
                count[ord(c)-ord("a")] += 1

            key = tuple(count)
            if key in hash:
                hash[key].append(s)
            else:
                hash[key] = [s]

        return list(hash.values())


        
# @leet end
