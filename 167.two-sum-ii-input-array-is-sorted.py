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
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPointer, rightPointer = 0, len(numbers) - 1
        while leftPointer != rightPointer:
            status = numbers[leftPointer] + numbers[rightPointer]
            if status < target:
                leftPointer += 1
            elif status > target:
                rightPointer -= 1
            else:
                return [leftPointer+1, rightPointer+1]

        
        return []
        
# @leet end
