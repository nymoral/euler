"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
from utils import PrimeGen

def sum_primes_below(limit):
    gen = PrimeGen(limit)
    return sum(gen)

if __name__ == "__main__":
    print(sum_primes_below(2000000))

