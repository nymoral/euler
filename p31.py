"""
In England the currency is made up of pound, £, and pence, p,
and there are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:
1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""

"""
200 = a*1 + b*2 + c*5 + d*10+ e*20 + f*50 + g*100 + h*200
"""

class Coin(object):

    def __init__(self, value, child):
        self.value = value
        self.child = child

    def solve(self, n):
        if self.child == None:
            if (n != 0) and (n % self.value == 0):
                return 1
            else:
                return 0
        current = 0
        for i in range(0, n+1, self.value):
            if i == n:
                current += 1
            else:
                current += self.child.solve(n-i)
        return current


def number_of_ways(n):
    a = Coin(1, None)
    b = Coin(2, a)
    c = Coin(5, b)
    d = Coin(10, c)
    e = Coin(20, d)
    f = Coin(50, e)
    g = Coin(100, f)
    h = Coin(200, g)

    return h.solve(200)

if __name__ == "__main__":
    print(number_of_ways(200))
