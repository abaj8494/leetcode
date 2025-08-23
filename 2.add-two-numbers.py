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
# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
        #self.val = val
        #self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # get numbers out:
        head = l1
        l1_nums = [] # [2,4,3]
        while head:
            l1_nums.append(head.val)
            head = head.next
        print("l1_nums:", l1_nums)
        head = l2
        l2_nums = [] # [5,6,4]
        while head:
            l2_nums.append(head.val)
            head = head.next
        print("l2_nums:", l2_nums)
        # reverse the lists and turn them into ints:
        if l1_nums is not None:
            l1_nums = list(reversed(l1_nums))
        if l2_nums is not None:
            l2_nums = list(reversed(l2_nums))
        l1_num = int(''.join(map(str, l1_nums))) #342
        l2_num = int(''.join(map(str, l2_nums))) #465
        sum = l1_num + l2_num
        sum_list = list(map(int, str(sum)))      # [8, 0, 7]
        #if sum_list is not None:
        #    sum_list = list(reversed(sum_list))  # [7, 0, 8]
        print(sum_list)

        # LN(7) <- LN(0) <- LN(8)

        tail = None
        for i in range(len(sum_list)):
            next = ListNode(sum_list[i], tail)
            i = i + 1
            tail = next

        return tail
        
# @leet end
