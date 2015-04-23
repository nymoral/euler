"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
3   ->
7 4 ->
2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom of the triangle below:
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
"""

def biggest_sum(triangle):
    triangle = triangle.split("\n")
    triangle = [t for t in triangle if t != ""]
    triangle = [[int(x) for x in t.split()] for t in triangle]
    
    # Flip the triangle upside down and expand each node thus:
    #  node in lowest level (0 in upside-down one) becomes (node)
    #  node (j) in others levels (i) becomes (node + max(level[i + 1][j], level[i + 1][j+1])), where we index the original triangle.
    #  The biggest path sum will be at the top of the original triangle (bottom of the upside-down one)
    triangle = triangle[::-1]

    for rid, row in enumerate(triangle):
        if rid != 0:
            for nid, node in enumerate(row):
                row[nid] = node + max(triangle[rid - 1][nid], triangle[rid - 1][nid + 1])
        #print(row)

    return triangle[-1][0]
    


if __name__ == "__main__":
    triangle = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""
    print(biggest_sum(triangle))
