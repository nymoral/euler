"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
    The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.
"""

def is_amicable(n, sums):
	b = sums[n]
	if b >= len(sums):
		return False
	a = sums[b]
	if a == b:
		return False
	return a == n


def sum_divisors(n):
	s = 1
	limit = int(n**0.5)
	if limit**2 == n:
		s += limit
		limit -= 1
	for i in range(2, limit+1):
		if n % i == 0:
			s += (i + n // i)
	return s

def sum_of_amicable(under):
	sum_of_divisors = [None for i in range(under)]
	for n in range(4, under):
		sum_of_divisors[n] = sum_divisors(n)

	r = 0
	for i, s in enumerate(sum_of_divisors):
		if s == None:
			continue
		if is_amicable(i, sum_of_divisors):
			r += i
	return r

    

if __name__ == "__main__":
    print(sum_of_amicable(10000))
