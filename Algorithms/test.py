import collections
def findLongestWord(s, d):
    """
    :type s: str
    :type d: List[str]
    :rtype: str
    """
    ans = []
    dmap = collections.defaultdict(list)
    for w in d:
        dmap[w[0]].append((0, w))
    for string in s:
        wlist = dmap[string]
        del dmap[string]
        for i, w in wlist:
            if i + 1 == len(w):
                ans.append(w)
            else:
                dmap[w[i + 1]].append((i + 1, w))
    if not ans: return ''
    maxl = len(max(ans, key=len))
    return min(w for w in ans if len(w) == maxl)
findLongestWord( "abpcplea",["ale","apple","monkey","plea"])