"""
* Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
* 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
* By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
class Fibo(object):
    def __init__(self, upto = "inf"):
        self.first = 0
        self.second = 1
        self.upto = upto

    def __iter__(self):
        return self

    def next(self):
        if self.second < self.upto:
            r = self.second
            self.first, self.second = self.second, self.first + self.second
            return r
        else:
            raise StopIteration()

    def __next__(self):
        return self.next()

def fibo_sum(upto):
    return sum(f for f in Fibo(upto) if ((f % 2) == 0))

if __name__ == "__main__":
    r = fibo_sum(4000000)
    print(r)
