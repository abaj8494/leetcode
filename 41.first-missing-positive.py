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
    def firstMissingPositive(self, nums: List[int]) -> int:
        """shockingly this code is accepted despite the O(nlogn) tc and O(n) sc
        # will remove this assumption later:
        nums = sorted(list(set(nums)))

        one = False
        location = 0
        for i, num in enumerate(nums):
            if num == 1:
                one = True
                location = i

        if one == False:
            return 1

        # check subsequent:
        j = location
        spi = 1
        while j < len(nums):
            if nums[j] == spi:
                spi += 1
                j += 1
                continue
            return spi
        return spi
        """

        # cyclic sort:
        n = len(nums)
        
        # place each positive integer at the respective index within nums
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] -1], nums[i] = nums[i], nums[nums[i] -1] # swap
        
        # linear search for first discrepancy
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1 # returns discrep
                
        # or returns n + 1
        return n + 1

        
# @leet end
