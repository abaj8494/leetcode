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
from itertools import combinations
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        combinations_of_3 = List(combinations(nums,3))
        print(len(combinations_of_3))
        out = []
        for c in combinations_of_3:
            if sum(c) == 0:
                if sorted(c) not in out:
                    out.append(sorted(c))

        return out
        
        
# @leet end
