def solveNQueens( n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    ans = []

    def DFS(queens, xy_dif, xy_sum):
        p = len(queens)
        if p == n:
            ans.append(queens)
        for q in range(n):
            if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                DFS(queens + [q], xy_dif + [p - q], xy_sum + [q + p])

    DFS([], [], [])
    return [['.' * i + 'Q' + '.' * (n - i - 1) for i in queen] for queen in ans]

solveNQueens(4)