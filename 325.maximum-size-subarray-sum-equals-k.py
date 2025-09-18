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
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        N = len(nums)

        current = 0
        lookup = {}
        lookup[0] = -1

        best = 0
        for index, x in enumerate(nums):
            current += x

            if current - k in lookup:
                left = lookup[current - k]
                right = index

                best = max(best, right - left)

            if current not in lookup:
                lookup[current] = index

        return best
        
# @leet end
