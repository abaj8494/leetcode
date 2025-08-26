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
    def isSubsequence(self, s: str, t: str) -> bool:
        """reasonably good, but not duplicate resistant code
        matched = 0
        str_idx = -1
        for s_char in s:
            for curr_idx, t_char in enumerate(t):
                if s_char == t_char:
                    if curr_idx > str_idx:
                        str_idx = curr_idx
                        matched += 1
                    else:
                        return False
        if matched == len(s):
            return True
        return False
        """
        matched = 0
        match_idx = 0
        for s_char in s:
            for curr_idx, t_char in enumerate(t[match_idx:]):
                if s_char == t_char:
                    matched += 1
                    match_idx += curr_idx + 1
                    break
        if matched == len(s):
            return True
        return False
# @leet end
