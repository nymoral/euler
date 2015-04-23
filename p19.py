"""
You are given the following information, but you may prefer to do some research for yourself.
1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

import datetime 

def nr_sundays(start, end):
    add = datetime.timedelta(days = 1)
    c = 0
    while start < end:
        if (start.day == 1) and (start.weekday() == 6):
            c += 1
        start += add
    return c

if __name__ == "__main__":
    start = datetime.date(1901, 1, 1)
    end = datetime.date(2000, 12, 31)
    print(nr_sundays(start, end))
