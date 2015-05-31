"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 × 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

from collections import Counter
from operator import mul
from functools import reduce
from copy import deepcopy


def is_identity_pandigital(i, n, base_set):
    digits = [int(c) for c in str(i)]
    c = Counter(digits)
    if 0 in c:
        return False
    digits_repeat = reduce(mul, c.values(), 1) != 1
    if digits_repeat:
       return False 
    limit = int(i**0.5)
    for d in range(1, limit):
        if i % d == 0:
            a = [int(digit) for digit in str(d)]
            b = [int(digit) for digit in str(i // d)]
            if 0 in a:
               continue
            if 0 in b:
               continue
            # a, b -- divisors
            tmp_counter = deepcopy(c)
            for digit in a:
                tmp_counter[digit] += 1
            for digit in b:
                tmp_counter[digit] += 1
            if len(tmp_counter) != n:
                continue
            if set(tmp_counter.values()) == base_set:
                return True
    return False


def sum_pandigital_products(n):
    """
    This one is very hackish.
    Pretty much brute force with a couple of safe checks.
    + I don't check every number up to 10**n.
    """

    s = 0
    base_set = set(1 for i in range(n))
    for i in range(100, int((10**n)**0.6)):
        if is_identity_pandigital(i, n, base_set):
            s += i
    return s
            

if __name__ == "__main__":
    print(sum_pandigital_products(9))

