"""
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def next_node(n):
    if n % 2 == 0:
        return n // 2
    else:
        return (3 * n) + 1

def calc_length(history, start):
    node = start
    f = None
    l = 0
    f = history.get(node, None)
    while f == None:
        node = next_node(node)
        f = history.get(node, None)
        l += 1
    l += f
    history[start] = l
    return l

def longest_chain_start(under):
    history = {1: 1}
    longest = 0
    n = 0
    for i in range(2, under):
        l = calc_length(history, i)
        if l > longest:
            n = i
            longest = l
    return n 



if __name__ == "__main__":
    print(longest_chain_start(1000000))
