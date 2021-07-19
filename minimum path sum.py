# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example:

# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.


import numpy as np

x = []
while(True):
    i = list(map(int, input()))
    if(len(i) > 0):
        x.append(i)
    else:
        break

print(np.array(x))


def minPathSum(grid):
    h = len(grid)
    w = len(grid[0])
    dp = [[0 for _ in range(w)] for _ in range(h)]
    for row in range(h):
        for col in range(w):
            if row == 0 and col == 0:
                dp[row][col] = grid[row][col]
            else:
                dp[row][col] = grid[row][col] + \
                    min((10000 if row == 0 else dp[row-1][col]),
                        (10000 if col == 0 else dp[row][col-1]))
    return dp[h-1][w-1]


print(minPathSum(x))
