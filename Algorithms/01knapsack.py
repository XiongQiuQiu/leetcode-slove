'''
N:nums of all goods
W: knapsack capacity
weights: goods weight
values: goods value
'''
def kanpsack(weights,values,W,N):
    dp = [0] * (W+1)
    for i in range(len(N)):
        w = weights[i]
        v = values[i]
        for j in range(len(W))[::-1]:
            dp[j] = max(dp[j],dp[j-w]+v)
    return dp[-1]