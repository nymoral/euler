"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

"""
We have:
    a^2 + b^2 = c^2
    a + b + c = 1000

    a + b = 1000 - c // ^2
    a^2 + b^2 + 2ab = 1000^2 - 2000c + c^2
    ^^^^^^^^^ == c^2
    
    c^2 + 2ab = 1000^2 - 2000c + c^2
    2ab = 1000^2 - 2000c
    ab = 500000 - 1000c

    We need to find abc, so we can look at ab = t as one variable

    t = 500000 - 1000c

    As t >= 2, 2 <= 500000 - 1000c, 1000c <= 499998
    c is Natural number, thus c <= 49
    3 <= c <= 499
"""

def tripletProduct():
    for c in range(3, 499 + 1):
        t = 500000 - (1000 * c)
        # a < b < c, a*b = t
        for a in range(1, c):
            if t % a == 0:
                b = t // a
                if a**2 + b**2 == c**2:
                    return (t*c)
    

if __name__ == "__main__":
    print(tripletProduct())


