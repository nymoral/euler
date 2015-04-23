import math

"""
* The prime factors of 13195 are 5, 7, 13 and 29.
* What is the largest prime factor of the number 600851475143 ?
"""
from utils import PrimeGen

def largest_prime_factor(num):
    p = PrimeGen()
    largest = 0
    limit = int(math.sqrt(num))
    for i in range(3, limit + 1, 2):
        if (num % i) == 0:
            if p.is_prime(i):
                largest = i
    return largest

if __name__ == "__main__":
    print(largest_prime_factor(600851475143))

