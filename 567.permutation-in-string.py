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
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        if len(s1) == len(s2) and set(s1) != set(s2): return False
        perms = [''.join(q) for q in itertools.permutations(s1)]

        res = False
        for perm in perms:
            print(perm)
            index = s2.find(perm, 0)
            if index != -1:
                res = True
        return res
        """
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        s1_counts = [0] * 26
        s2_counts = [0] * 26


        for i in range(n1):
            s1_counts[ord(s1[i])-ord('a')] += 1
            s2_counts[ord(s2[i])-ord('a')] += 1

        if s1_counts == s2_counts:
            return True

        for i in range(n1, n2):
            s2_counts[ord(s2[i]) - ord('a')] += 1
            s2_counts[ord(s2[i - n1]) - ord('a')] -= 1
            if s1_counts == s2_counts:
                return True
        return False
        
# @leet end
