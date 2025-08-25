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
    def majorityElement(self, nums: List[int]) -> int:
        """my naive soln
            d = {x:nums.count(x) for x in nums}
            a, b = d.keys(), d.values()
            max_value = max(b)
            max_index = list(b).index(max_value)
            return (list(a)[max_index])

            # o(n^2) because we run o(n) count on each x
        """

        """
        candidate = 0
        count = 0
        # phase 1: find candidate
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
        """
        count = {} # dictionary.
        res, maxCount = 0, 0
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            res = n if count[n] > maxCount else res
            maxCount = max(count[n], maxCount)

        return res
        
# @leet end
