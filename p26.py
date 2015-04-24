"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
    1/2 =   0.5
    1/3 =   0.(3)
    1/4 =   0.25
    1/5 =   0.2
    1/6 =   0.1(6)
    1/7 =   0.(142857)
    1/8 =   0.125
    1/9 =   0.(1)
    1/10    =   0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

max_s = 100

def rep_len(n):
    # http://mathworld.wolfram.com/DecimalExpansion.html
    for s in range(max_s):
        for t in range(1, n):
            if 10**s == (10**(s+t)) % n:
                return t
    return -1

def longest_d(limit):
    m = 1
    d = -1
    for n in range(2, limit):
        # In base-10 it's factors 2 and 5 will not produce recurring cycles. 3 won't produce anything of significant lenth. 
        # Calculation is crazy slow without this.
        if n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
            r = rep_len(n)
            if r > m:
                m = r
                d = n
    return d


if __name__ == "__main__":
    print(longest_d(1000))
