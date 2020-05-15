#!/usr/bin/env python
# coding: utf-8

import statistics as stat
import copy
from decimal import Decimal, getcontext

def midrange(nums):
    nums_sort = copy.copy(nums)
    nums_sort.sort()
    low, high = nums_sort[0], nums_sort[-1]
    if type(low) and type(high) is int:
        return (low + high) // 2
    if type(low) or type(high) is float:
        return (low + high) / 2

def nrange(nums):
    nums_sort = copy.copy(nums)
    nums_sort.sort()
    low, high = nums_sort[0], nums_sort[-1]
    return high - low

def IQR(nums):
    nums_sort = copy.copy(nums)
    nums_sort.sort()
    q1 = stat.median(nums_sort[0:len(nums)//2])
    if len(nums)%2 == 0:
        q3 = stat.median(nums_sort[len(nums)//2:])
    if len(nums)%2 == 1:
        q3 = stat.median(nums_sort[len(nums)//2+1:])
    return float(Decimal(q3) - Decimal(q1))

while True:
    print("Enter in numbers separated by spaces: ")
    print("Type 'exit' to exit.")
    nums = input()

    if nums == 'exit':
        break
    
    nums = nums.split()
    nums = [x.strip() for x in nums]
    # finds the longest numbers and saves the length to a variable
    longest_num = len(Decimal(max(nums, key=len)).as_tuple().digits)
    getcontext().prec = longest_num
    
    
    try:
        nums = [float(x) if '.' in x else int(x) for x in nums]
    except Exception as x:
        print(x, "\n" + "Numbers only.")
        break

    while True:
        print("Enter in how to calculate." +
              "(Mean, Median, Mode, Midrange, Range, IQR)")
        print("Type 'exit' to exit.")
        calc = input().strip().lower()

        if calc == 'exit':
            break
        if calc == 'mean':
            print(stat.mean(nums))
        elif calc == 'median':
            print(stat.median(nums))
        elif calc == 'mode':
            try:
                print(stat.mode(nums))
            except:
                print("No value is found more than once.")
        elif calc == 'midrange':
            print(midrange(nums))
        elif calc == 'range':
            print(nrange(nums))
        elif calc == 'iqr':
            print(IQR(nums))
        
