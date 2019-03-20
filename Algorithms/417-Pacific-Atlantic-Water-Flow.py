'''
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
'''


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        cl, rl = len(matrix), len(matrix[0]) if len(matrix) else 0
        p = set([(0, i) for i in range(rl)] + [(i, 0) for i in range(cl)])
        a = set([(cl - 1, i) for i in range(rl)] + [(i, rl - 1) for i in range(cl)])

        def bfs(vset):
            dz = zip((0, 1, 0, -1), (-1, 0, 1, 0))
            queue = list(vset)
            while queue:
                x, y = queue.pop(0)
                for dx, dy in dz:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < cl and 0 <= ny < rl:
                        if matrix[nx][ny] >= matrix[x][y]:
                            if (nx, ny) not in vset:
                                queue.append((nx, ny))
                                vset.add((nx, ny))

        bfs(p)
        bfs(a)
        result = p & a
        return map(list, result)
