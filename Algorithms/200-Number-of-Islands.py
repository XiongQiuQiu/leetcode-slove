'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ans = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    self.bfs(grid, x, y)
                    ans += 1
        return ans

    def bfs(self, grid, x, y):
        dxs = [1, 0, -1, 0]
        dys = [0, 1, 0, -1]
        queue = [(x, y)]
        grid[x][y] = 0
        while queue:
            x, y = queue.pop(0)
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    if grid[nx][ny] == '1':
                        grid[nx][ny] = 0
                        queue.append((nx, ny))
        return 1

