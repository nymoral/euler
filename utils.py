import math

class PrimeGen(object):
    def __init__(self, limit = "inf"):
        self.primes = [2, 3, 5, 7, 11, 13, 17, 19]
        self.reset()
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def is_prime(self, n):
        r = self.sieve_check(n)
        if r != None:
            return r
        # We ran out of numbers
        limit = int(math.sqrt(n))
        while True:
            new = self.increase()
            if n % new == 0:
                return False
            if new >= limit:
                return True

    def sieve_check(self, n):
        limit = int(math.sqrt(n))
        for p in self.primes:
            if n % p == 0:
                return False
            if p >= limit:
                return True
        return None

    def increase(self):
        candidate = self.primes[-1]
        candidate += 2

        while( False == self.sieve_check(candidate) ):
            candidate += 2

        self.primes.append(candidate)
        return candidate

    def reset(self):
        self.index = 0
        
    def next(self):
        self.index += 1
        r = 0
        if self.index <= len(self.primes):
            r = self.primes[self.index - 1]
        else:
            r = self.increase()
        if r >= self.limit:
            raise StopIteration()
        return r

