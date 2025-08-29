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
#from itertools import combinations
"""
class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(numbers: List[int], target: int) -> List[List[int]]:
            res = []
            if not numbers:
                return []
            leftPointer, rightPointer = 0, len(numbers) - 1
            while leftPointer < rightPointer:
                status = numbers[leftPointer] + numbers[rightPointer]
                if status < target:
                    leftPointer += 1
                elif status > target:
                    rightPointer -= 1
                else:
                    res.append([leftPointer + 1, rightPointer + 1])

                    # skip duplicates on BOTH sides
                    lv, rv = numbers[leftPointer], numbers[rightPointer]
                    while leftPointer < rightPointer and numbers[leftPointer] == lv:
                        leftPointer += 1
                    while leftPointer < rightPointer and numbers[rightPointer] == rv:
                        rightPointer -= 1
            
            return res
        #combinations_of_3 = list(combinations(nums,3))
        #print(len(combinations_of_3))
        #out = []
        #for c in combinations_of_3:
        #    if sum(c) == 0:
        #        if sorted(c) not in out:
        #            out.append(sorted(c))
        #
        #return out

        nums.sort()
        out = []
        for i,n in enumerate(nums):
            if n>0:
                break # sorted, so a positive number means we can never get to 0
            if i>0 and n == nums[i-1]: # skip if same as previous
                continue
            print(nums[i+1:])
            idxs = twoSum(nums[i+1:], 0-n)
            if idxs:
                for idx in idxs: 
                    out.append([n, nums[i+idx[0]], nums[i+idx[1]]])

        return out
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(numbers: List[int], target: int) -> List[List[int]]:
            res: List[List[int]] = []
            if not numbers:
                return res
            leftPointer, rightPointer = 0, len(numbers) - 1

            while leftPointer < rightPointer:
                status = numbers[leftPointer] + numbers[rightPointer]
                if status < target:
                    leftPointer += 1
                elif status > target:
                    rightPointer -= 1
                else:
                    # record (keeping your 1-based indexing)
                    res.append([leftPointer + 1, rightPointer + 1])

                    # skip duplicates on BOTH sides
                    lv, rv = numbers[leftPointer], numbers[rightPointer]
                    while leftPointer < rightPointer and numbers[leftPointer] == lv:
                        leftPointer += 1
                    while leftPointer < rightPointer and numbers[rightPointer] == rv:
                        rightPointer -= 1
            return res

        nums.sort()
        out: List[List[int]] = []

        for i, n in enumerate(nums):
            if n > 0:
                break  # remaining numbers are positive → no more triplets
            if i > 0 and n == nums[i - 1]:
                continue  # skip duplicate anchors

            idxs = twoSum(nums[i + 1:], -n)  # search suffix
            for l1, r1 in idxs:               # l1/r1 are 1-based within the suffix
                out.append([n, nums[i + l1], nums[i + r1]])

        return out

# @leet end
