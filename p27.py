"""
Euler discovered the remarkable quadratic formula:
n² + n + 41
It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39.
However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.
The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79.
The product of the coefficients, −79 and 1601, is −126479.
Considering quadratics of the form:
n² + an + b, where |a| < 1000 and |b| < 1000
where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b,
for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""

from utils import PrimeGen

def nr_primes_generated(a, b, primes):
    nr_primes = 0
    for n in range(300):
        p = n**2 + a*n + b
        if p not in primes:
            return nr_primes
        nr_primes += 1
    return nr_primes

def best_coefficients_product(a_max, b_max):
    # Generate ~ 80k primes to check against.
    primes = {prime for prime in PrimeGen(10**6)}
    max_primes = -1
    best_product = 0
    for a in range(-a_max + 1, a_max):
        for b in range(-b_max + 1, b_max):
            n = nr_primes_generated(a, b, primes)
            if n > max_primes:
                max_primes = n
                best_product = a * b
    return best_product 
                




if __name__ == "__main__":
    print(best_coefficients_product(1000, 1000))
