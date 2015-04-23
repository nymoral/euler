"""
* If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
* Find the sum of all the multiples of 3 or 5 below 1000.
"""
def sum_multiples(mul, below):
    first = mul                             # First multiple of mul
    last = ((below - 1) // mul) * mul       # The last multiple of mul
    n = ((last - first) // mul) + 1         # The number of multiples
    return (n * (first + last)) // 2        # Arithmetic progression sum

def sum_multiples_3_5(below):
    sum3 = sum_multiples(3, below)
    sum5 = sum_multiples(5, below)
    sum15 = sum_multiples(15, below)
    return sum3 + sum5 - sum15


if __name__ == "__main__":
    r = sum_multiples_3_5(1000)
    print(r)

