

def findCircleNum(M):
    """
    :type M: List[List[int]]
    :rtype: int
    """
    cnt = 0
    for r in range(len(M)):
        for c in range(len(M[0])) :
            print r,c
            if M[r][c] == 1:
                cnt += one(M,(r,c))
    return cnt

def one(M,point):
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    queue = [point]
    M[point[0]][point[1]] = 0
    while queue:
        x,y = queue.pop()
        for tx,ty in zip(dx,dy):
            nx = x+tx
            ny = y+ty
            if 0 <= nx<len(M) and 0 <= ny < len(M[0]):
                if M[nx][ny] == 1:
                    M[nx][ny] = 0
                    queue.append((nx,ny))
    return 1

findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
[[1,0,0,1],
 [0,1,1,0],
 [0,1,1,1],
 [1,0,1,1]]