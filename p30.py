"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

def is_made_of_pow(n):
	return n == sum(int(i)**5 for i in str(n))

def sum_fifth_pow_nums():
	# I tested 10^5, 10^6 and 10^7. 5 < 6 = 7
	return sum(i for i in range(2, 10**6) if is_made_of_pow(i))


if __name__ == "__main__":
    print(sum_fifth_pow_nums())

