"""
In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. 
We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well. 

At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid.
A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.

What is the maximum total sum that the height of the buildings can be increased?
"""


def max_increase_keeping_skyline(grid):
    """
    Time complexity -> O(n^2)
    Space complexity -> O(n)
    """
    skyline_top = [max(row) for row in zip(*grid)]
    skyline_left = [max(row) for row in grid]

    increase = 0

    for i, row in enumerate(grid):
        for j, building in enumerate(row):
            if building < min(skyline_top[j], skyline_left[i]):
                increase += min(skyline_top[j], skyline_left[i]) - building

    return increase
