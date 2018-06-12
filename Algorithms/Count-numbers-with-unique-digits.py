def count_number(n):
    f = [0 for i in range(n+1)]
    g = [0 for i in range(n+1)]
    ans = 10
    g[0], g[1] = 1, 9
    for i in range(2, n+1):
        f[i] = f[i-1] * (11 - i) + g[i-1]
        g[i] = g[i-1] * (10 - i)
        ans += f[i] + g[i]
    return ans

print count_number(3)