#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    count = 0
    empty_Set = set()                    # Assigning an empty set
    for i in range(len(ar)):
        if ar[i] not in empty_Set:
            empty_Set.add(ar[i])         # Adding values in set
        else:
            count += 1 
            empty_Set.remove(ar[i])
    return count      
         

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
