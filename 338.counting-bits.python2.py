# @leet imports start
from bisect import *
from collections import *
from copy import *
from datetime import *
from heapq import *
from math import *
from re import *
from string import *
from random import *
from itertools import *
from functools import *
from operator import *
import string
import re
import datetime
import collections
import heapq
import bisect
import copy
import math
import random
import itertools
import functools
import operator
# @leet imports end

# @leet start
class Solution(object):
    def countBits(self, n: int):
        ans = []

        for i in range(n+1):
            temp = bin(i)
            ans.append(str(temp)[2:].count('1'))

        return ans


        
# @leet end
