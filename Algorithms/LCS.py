# -*- coding:utf-8 -*-
"""
Longest Common Subsequences
"""


'''最长公共子序列长度'''
def lcs1(s1, s2):
    ls1, ls2 = len(s1), len(s2)
    if ls1 < 1 or ls2 < 1: return 0
    if s1[ls1 - 1] == s2[ls2 - 1]: return lcs1(s1[:-1], s2[:-2]) + 1
    return max(lcs1(s1[:-1], s2), lcs1(s1, s2[:-1]))

def minDistance(self, w1, w2):
    m, n = len(w1), len(w2)
    dp = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(m):
        for j in range(n):
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], dp[i][j] + (w1[i] == w2[j]))
    return m + n - 2 * dp[m][n]


'''最长公共子序列'''
def lcs2(s1, s2):
    lens1 = len(s1)
    lens2 = len(s2)
    c = [[0 for i in range(lens2+1)] for j in range(lens1+1)]
    flag = [[0 for i in range(lens2+1)] for j in range(lens1+1)]
    for i in range(1, lens1+1):
        for j in range(1, lens2+1):
            if s1[i-1] == s2[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                flag[i][j] = 'ok'
            elif c[i][j-1] > c[i-1][j]:
                c[i][j] = c[i][j-1]
                flag[i][j] = 'left'
            else:
                c[i][j] = c[i-1][j]
                flag[i][j] = 'up'
    return c, flag


def printLcs(flag, a, i, j):
    if i == 0 or j == 0 :
        return
    if flag[i][j] == 'ok':
        printLcs(flag, a, i-1, j-1)
        print a[i-1]
    elif flag[i][j] == 'left':
        printLcs(flag, a, i, j-1)
    else:
        printLcs(flag, a, i-1, j)



'''最长公共子串'''
class LCS:
    def lcs_dp(self, input_x, input_y):
        dp = [[0 for i in range(len(input_x))] for j in range(len(input_y))]
        maxlen = maxindex = 0
        for i in range(0, len(input_x)):
            for j in range(0, len(input_y)):
                if input_x[i] == input_y[j]:
                    if i != 0 and j != 0:
                        dp[i][j] = dp[i-1][j-1] + 1
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    if dp[i][j] > maxlen:
                        maxlen = dp[i][j]
                        maxindex = i + 1 - maxlen
        return input_x[maxindex:maxindex + maxlen]


if __name__ == '__main__':
    # print lcs1('abcde', 'oaob')

    a = 'ABCBDAB'
    b = 'BDCABA'
    c, flag = lcs2(a, b)
    for i in c:
        print(i)
    print('')
    for j in flag:
        print(j)
    print('')
    printLcs(flag, a, len(a), len(b))
    print('')