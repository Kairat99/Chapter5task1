#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def abbreviation(a, b):
    regexp = '^[a-z]*%s[a-z]*$' % '[a-z]*'.join('[%s%s]' % (letter, letter.lower()) for      letter in b)
    
    if re.search(regexp, a):
        return 'YES'
    else:
        return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()