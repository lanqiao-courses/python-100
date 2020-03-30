class Solution(object):

    def island_perimeter(self, grid):
        if grid is None:
            raise TypeError('grid cannot be None')
        sides = 0
        num_rows = len(grid)
        num_cols = len(grid[0])
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 1:
                    # Check left
                    if j == 0 or grid[i][j - 1] == 0:
                        sides += 1
                    # Check right
                    if j == num_cols - 1 or grid[i][j + 1] == 0:
                        sides += 1
                    # Check up
                    if i == 0 or grid[i - 1][j] == 0:
                        sides += 1
                    # Check down
                    if i == num_rows - 1 or grid[i + 1][j] == 0:
                        sides += 1
        return sides