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
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums_str = str(nums)
        nums_set = set(nums)
        ans = []
        for i in nums_set:
            if nums_str.count(str(i)) == 1:
                ans.append(i)


        return ans


        
# @leet end
