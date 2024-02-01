import math
import os
import random
import re
import sys

def weird_or_not(n):
    if n % 2 == 1:
        return "Weird"
    elif n % 2 == 0 and 2 <= n <= 5:
        return "Not Weird"
    elif n % 2 == 0 and 6 <= n <= 20:
        return "Weird"
    elif n % 2 == 0 and n > 20:
        return "Not Weird"

            
if __name__ == '__main__':
    n = int(input().strip())
    result = weird_or_not(n)
    print(result)

