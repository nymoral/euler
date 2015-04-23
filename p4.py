"""
* A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
* Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(n):
    return str(n) == str(n)[::-1]


def largest_palindrome(start, end):
    largest = 0
    for i in range(start, end+1):
        for j in range(i, end+1):
            p = i * j
            if is_palindrome(p):
                if p > largest:
                    largest = p
    return largest

if __name__ == "__main__":
    print(largest_palindrome(100, 999))
