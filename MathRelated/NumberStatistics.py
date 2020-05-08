#!/usr/bin/env python
# coding: utf-8

import statistics as stat
import copy

while True:
    print("Enter in numbers separated by comma(s): ")
    print("Type 'exit' to exit.")
    nums = input()

    if nums == 'exit':
        break
    nums = nums.split(',')
    nums = [x.strip() for x in nums]

    try:
        nums = [float(x) if '.' in x else int(x) for x in nums]
    except Exception as x:
        print(x, "\n" + "Numbers only.")
        break

    while True:
        print("Enter in how to calculate." +
              "(Mean, Median, Mode, Midrange, Range)")
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
            nums_sort = copy.copy(nums)
            nums_sort.sort()
            low, high = nums_sort[0], nums_sort[-1]
            print(low + high / 2)
        elif calc == 'range':
            nums_sort = copy.copy(nums)
            nums_sort.sort()
            low, high = nums_sort[0], nums_sort[-1]
            print(high - low)
