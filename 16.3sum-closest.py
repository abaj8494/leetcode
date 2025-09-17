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

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums = sorted(nums)

        n = len(nums)
        closest_sum = 9999999

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            lo, hi = i + 1, n - 1

            while lo < hi:
                cur_sum = nums[i] + nums[lo] + nums[hi]

                if abs(cur_sum - target) < abs(closest_sum - target):
                    closest_sum = cur_sum

                if cur_sum == target:
                    return cur_sum
                elif cur_sum < target:
                    lo += 1
                else:
                    hi -= 1

        return closest_sum

                
            





        
# @leet end
