
def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    cl = len(board)
    rl = len(board[0]) if cl else 0
    for c in range(cl):
        for r in range(rl):
            if board[c][r] == word[0]:
                if len(word) == 1: return True
                if helper(board, (c, r,1), word, cl, rl):
                    return True
    return False

def helper( board, point, word, cl, rl):
    dz = zip((0, 1, 0, -1), (-1, 0, 1, 0))
    queue = [point]
    vset = {point[:2]}
    while queue:
        x, y, i = queue.pop()
        for dx, dy in dz:
            nx, ny = dx + x, dy + y
            if 0 <= nx < cl and 0 <= ny < rl and (nx, ny) not in vset:
                if board[nx][ny] == word[i]:
                    if i == len(word) - 1:
                        return True
                    queue.append((nx, ny, i + 1))
                    vset.add((nx, ny))

    return False


exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],
"ABCESEEEFS")