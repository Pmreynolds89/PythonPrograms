import statistics as stat
import math
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

def IQR(nums, q = None):
    nums_sort = copy.copy(nums)
    nums_sort.sort()
    q1 = stat.median(nums_sort[0:len(nums)//2])
    if len(nums)%2 == 0:
        q3 = stat.median(nums_sort[len(nums)//2:])
    if len(nums)%2 == 1:
        q3 = stat.median(nums_sort[len(nums)//2+1:])
    
    if q == '1':
        return float(Decimal(q1))
    if q == '3':
        return float(Decimal(q3))
    else:
        return float(Decimal(q3) - Decimal(q1))

def variance(nums):
    numean = stat.mean(nums)
    varcal = list(map(lambda x: (x - numean)**2, nums))
    variance = sum(varcal) / (len(nums) - 1) 
    return variance

def zscore(znum, nums):
    numean = stat.mean(nums)
    zcal = (znum - numean) / math.sqrt(variance(nums)) 
    return zcal

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
              "(Mean, Median, Mode, Midrange, Range, IQR, Variance, Standard Deviation, Z Score)")
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
            print('If you want the quartiles, type \'IQR q1\' or \'IQR q3\'')
            print(IQR(nums))
        elif calc == 'iqr q1':
            q = '1'
            print(IQR(nums, q))
        elif calc == 'iqr q3':
            q = '3'
            print(IQR(nums, q))
        elif calc == 'variance':
            print(variance(nums))
        elif calc == 'standard deviation':
            print(math.sqrt(variance(nums)))
        elif calc == 'z score':
            print('Type which number to get the Z score of.')
            znum = input()
            try:
                if '.' in znum:
                    znum = float(znum)
                else:
                    znum = int(znum)
            except Exception as x:
                print(x, "\n" + "Numbers only.")
                break
            print(zscore(znum, nums))
        else:
            print('Please check that your calculation command is spelled' + 
                  ' correctly and contains a space between words.')
        
