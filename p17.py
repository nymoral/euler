"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""

def nr_letters_in_num(n):
    c = {0: 0,
         1: 3,
         2: 3,
         3: 5,
         4: 4,
         5: 4,
         6: 3,
         7: 5,
         8: 5,
         9: 4,
         10: 3,
         11: 6,
         12: 6,
         13: 8,
         14: 7,
         15: 7,
         16: 7,
         17: 9,
         18: 9,
         19: 8,
         20: 6,
         30: 6,
         40: 5,
         50: 5,
         60: 5,
         70: 7,
         80: 6,
         90: 6,
         100: 7,
         1000: 8,
         "and": 3
         }
    if n == 1000:
        return c[1] + c[1000]
    h = n // 100
    rem = n % 100
    count = 0
    if h > 0:
        count += c[h]
        #print("HUNDREDS", c[h])
        count += c[100]
        #print("H", c[100])
        if rem > 0:
            count += c["and"]
            #print("AND", c["and"])
    if rem > 20:
        t = rem // 10
        rem = rem % 10
        count += c[t * 10]
        #print("TENS", c[t * 10])
        count += c[rem]
        #print("ONES", c[rem])
    else:
        count += c[rem]
        #print("TEENS/ONES", c[rem])
        #print(rem)
    return count


def nr_letters_used_in_range(start, end):
    return sum(nr_letters_in_num(i) for i in range(start, end+1))

if __name__ == "__main__":
    print(nr_letters_in_num(1000))
    print(nr_letters_used_in_range(1, 1000))
