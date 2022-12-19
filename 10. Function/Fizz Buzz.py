#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    i = 1
    while i <= n:
        if i % 3 == 0:
            print("Fizz", end="")
            if i % 5 == 0:
                print("Buzz", end="")
        elif i % 5 == 0:
            print("Buzz", end="")
        else:
            print(i, end="")
        print()
        i += 1


n = int(input())
print(fizzBuzz(n))
