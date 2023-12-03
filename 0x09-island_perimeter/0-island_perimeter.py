#!/usr/bin/python3
"""Island Perimeter Problem"""

def island_perimeter(grid):
    """
    Function that returns the perimeter of the island described in grid
    """
    rows = len(grid)
    cols = len(grid[0])
    """
    The perimeter of an island is the sum of the number of edges
    that are not in contact with another island.
    """
    perimeter = 0
    
    """
    Iterate over the grid and check if the current cell is an island.
    If it is, check if it has a neighbour to the left or above.
    If it does, subtract 2 from the perimeter because the current cell
    is in contact with another island.
    """
    for i in range(rows):
        for j in range(cols):
            """
            If the current cell is an island, add 4 to the perimeter.
            """
            if grid[i][j] == 1:
                perimeter += 4
                """
                If the current cell is on the first row or column, it doesn't
                have a neighbour to the left or above, so we don't need to
                check for that.
                """
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
    """
    Return the perimeter of the island.
    """
    return perimeter
