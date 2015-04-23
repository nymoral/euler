"""
* The sum of the squares of the first ten natural numbers is,
* 1^2 + 2^2 + ... + 10^2 = 385
* The square of the sum of the first ten natural numbers is,
* (1 + 2 + ... + 10)^2 = 552 = 3025
* Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
* Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sum_of_squares(l):
    return sum(x**2 for x in l)

def square_of_sum(l):
    return sum(l)**2

def diferance(first, last):
    return square_of_sum(range(first, last + 1)) - sum_of_squares(range(first, last+1))

if __name__ == "__main__":
    print(diferance(1, 100))
