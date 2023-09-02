#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    x= s[0].upper()
    for i in range(1,len(s)):
        if s[i-1]==' ' and s[i].isalpha():
            x=x+s[i].upper()
        else:
            x=x+s[i]
    return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
