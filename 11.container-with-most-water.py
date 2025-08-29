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
    def maxArea(self, height: List[int]) -> int:
        """
        sorted_indices = sorted(range(len(height)), 
                                key=lambda index: height[index], reverse=True)
        maxArea = 0
        print(sorted_indices)
        for i, s in enumerate(sorted_indices):
            for j, t in enumerate(sorted_indices):
                if j >= i:
                    container_height = min(height[s],height[t])
                    area = abs(s-t) * container_height
                    if area > maxArea:
                        maxArea = area

        return maxArea

        # Time Limit Exceeded | 54/65 testcases passed
        """
        # two pointer approach
        maxArea = 0
        leftPointer = 0
        rightPointer = len(height)-1
        while leftPointer != rightPointer:
            area = min(height[leftPointer],height[rightPointer]) * abs(leftPointer - rightPointer)
            if area > maxArea:
                maxArea = area
            if height[leftPointer] < height[rightPointer]:
                leftPointer += 1
            else:
                rightPointer -= 1

        return maxArea




        
# @leet end
