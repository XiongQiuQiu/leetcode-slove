def reconstructQueue(people):
    """
    :type people: List[List[int]]
    :rtype: List[List[int]]
    """
    people.sort(key=lambda x: (x[1], x[0]))
    ans = []
    for i, p in enumerate(people):
        if p[1] == 0 or p[1] >= len(ans):
            ans.append(p)
            continue
        n = 0
        for i, k in enumerate(ans):
            if k[0] >= p[0] and n + 1 == p[1]:
                n += 1
            elif k[0] >= p[0] and n + 1 < p[1]:
                n += 1
            elif k[0] >= p[0] and n + 1 > p[1]:
                ans.insert(i, p)
                break
            if i == len(ans) - 1:
                ans.append(p)
                break
    return ans

print reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])