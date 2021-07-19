# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3

import numpy as np

x = []
while(True):
    i = list(map(int, input()))
    if(len(i) > 0):
        x.append(i)
    else:
        break

print(np.array(x))


def numIslands(grid):
    if len(grid) == 0:
        return 0
    h = len(grid)
    w = len(grid[0])
    answer = 0
    def inside(row, col): return 0 <= row and row < h and 0 <= col and col < w
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    vis = [[0 for _ in range(w)] for _ in range(h)]
    for row in range(h):
        for col in range(w):
            if not vis[row][col] and grid[row][col] == 1:
                answer += 1
                queue = []
                queue.append((row, col))
                vis[row][col] = 1
                while(len(queue)):
                    p = queue[0]
                    queue.pop(0)
                    for d in dir:
                        new_row = p[0] + d[0]
                        new_col = p[1] + d[1]
                        if inside(new_row, new_col) and not vis[new_row][new_col] and grid[new_row][new_col] == 1:
                            queue.append((new_row, new_col))
                            vis[new_row][new_col] = 1
    return answer


output = numIslands(x)

print(f'number of islands is: {output}')
