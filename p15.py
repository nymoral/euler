"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""

# We can get to a (i,j) point from (i-1, j) and (i, j - 1) points, where i, j > 0
# We can get to (i, 0) and (0, j) only with a single path going horizontaly or verticaly.

def nr_paths_with_history(history, x, y):
    index = (x, y)
    if (x == 0) or (y == 0):
        history[index] = 1
        print(index, 1)
        return 1
    f = history.get(index)
    if f == None:
        f = nr_paths_with_history(history, x - 1, y) + nr_paths_with_history(history, x, y - 1)
        history[index] = f
    print(index, f)
    return f


def nr_paths(x, y):
    history = {}
    return nr_paths_with_history(history, x, y)


if __name__ == "__main__":
    size = 20
    print(nr_paths(size, size))
