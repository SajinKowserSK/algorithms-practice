#!/bin/python

import math
import os
import random
import re
import sys


#
# Complete the 'efficientJanitor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts FLOAT_ARRAY weight as parameter.
#

def efficientJanitor(weight):
    weight.sort()
    left = 0
    right = len(weight) - 1
    count = 0

    while (left <= right):
        if (left == right):
            count += 1
            break

        if weight[left] + weight[right] <= 3:
            left += 1
            right -= 1
            count += 1

        else:
            right -= 1
            count += 1

    return count


# !/bin/python

import math
import os
import random
import re
import sys


#
# Complete the 'sortRoman' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY names as parameter.
#

def sortRoman(names):
    # Write your code here

    d, R, res = {}, {}, []
    for i in names:
        p = i.split(" ")
        k = convert(p[1])
        if k not in R:
            R[k] = p[1]
        if p[0] not in d:
            d[p[0]] = [k]
        else:
            d[p[0]].append(k)

    for i in sorted(d.keys()):
        res_str = i
        d[i].sort()
        for j in d[i]:
            res_str += " " + R[j]
            res.append(res_str)
            res_str = i
    return res


def convert(s):
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    z = 0
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i + 1]]:
            z -= roman[s[i]]
        else:
            z += roman[s[i]]
    return z + roman[s[-1]]

