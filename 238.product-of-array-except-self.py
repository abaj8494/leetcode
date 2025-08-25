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
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """o(n^2)
        res = [1] * len(nums)
        for i,num in enumerate(nums):
            for j in range(len(nums)):
                res[j] *= (num if i !=j  else 1)

        return res
        """

        """better code, but still not fast enough
        # calculate prefix
        prefix = [0] * (len(nums) + 2)
        prefix[0], prefix[len(nums)+1] = 1,1
        for i in range(len(nums)):
            prefix[i+1] = (nums[i] * prefix[i])

        print(prefix)

        # calculate postfix
        postfix = [0] * (len(nums) + 2)
        postfix[0], postfix[len(nums)+1] = 1,1
        print(postfix)
        for i in reversed(range(len(nums))):
            postfix[i+1] = (nums[i] * postfix[i+2])

        print(postfix)
        # multiply prefix with postfix for each n
        res = [0] * len(nums)
        for i in range(len((nums))):
            print(res)
            res[i] = prefix[i] * postfix[i+2]

        return res
        """

        # the issue above was space complexity.
        # we are going to update the result array for both prefix and postfix

        res = [1] * len(nums)
        # prefix loop:
        for i in range(1, len(nums)):
            res[i] = nums[i-1] * res[i-1]

        postfix = 1
        for j in reversed(range(len(nums)-1)):
            postfix *= nums[j+1]
            res[j] *= postfix


        return res
# @leet end
