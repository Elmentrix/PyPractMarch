#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.

neg = []
pos = []
zero = []

def plusMinus(arr):    
    # running a loop through the array to get the items from it
    for i in arr:
        if i > 0:
            pos.append(i)
        elif i < 0:
            neg.append(i)
        else:
            zero.append(i)
    
    # checking for the sizes into new variables
    size_pos = len(pos)
    size_neg = len(neg)
    size_zero = len(zero)
    
    # working on the ratios
    ratio_pos  = size_pos/n
    ratio_neg = size_neg/n
    ration_zero = size_zero/n
    
    # displaying the ratios in 6 decimal places
    print("%.6f" %ratio_pos)
    print("%.6f" %ratio_neg)
    print("%.6f" %ration_zero)
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
