"""
* By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
* What is the 10 001st prime number?
"""

from utils import PrimeGen

def nth_prime(n):
    p = PrimeGen()
    r = 0
    for i in range(n):
        r = p.next()
    return r

if __name__ == "__main__":
    print(nth_prime(10001))
