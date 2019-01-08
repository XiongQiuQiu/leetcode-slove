def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    ans = []


    def dfs(ans, stack, s):
        if not s:
            ans.append(stack)
        for i in range(len(s)):
            if i == 0 and 0 < int(s[i]) <= 10:
                dfs(ans, stack + [s[i]], s[i + 1:])
            if i == 1 and 10 <= int(s[:i + 1]) <= 26:
                dfs(ans, stack + [s[:i + 1]], s[i + 1:])

    dfs(ans, [], s)
    return len(ans)


numDecodings('100')