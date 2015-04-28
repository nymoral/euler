"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13
It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

def si(i):
    """
    Sum of i-th square corners from the center
    Eg: si(1) = 9 + 7 + 5 + 3
    """
    return 4*((1 + 2*i)**2) - 12*i

def spiral_diag_sum(side):
    n = side//2
    # 1 for center. It only apears once.
    return 1 + sum(si(i) for i in range(1, n+1))

if __name__ == "__main__":
    print(spiral_diag_sum(1001))
