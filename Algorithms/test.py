def combinationSum3(k, n):
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    ans = []

    def dfs(ans, stack, target, l,s):
        for i in range(s, 11):
            if target == 0 and l == 0:
                ans.append(stack[:])
                return
            if target-i < 0 or l-1 < 0:
                return
            dfs(ans, stack+[i], target - i, l - 1,i+1)
    dfs(ans, [], n, k,1)
    return ans
print combinationSum3(3,15)