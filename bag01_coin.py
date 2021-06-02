# 0-1背包和硬币找零问题，硬币找零还没写
def bag01(weights, values, capacity):
    num = len(weights)
    dp = [[0] * (num+1) for i in range(capacity+1)]
    for i in range(capacity+1):
        dp[i][0] = 0
    for i in range(num+1):
        dp[0][i] = 0
    for i in range(1, capacity+1): #i,j 表示第几个，而不是下标索引
        for j in range(1, num+1):
            # dp[i][j-1], dp[i-weights[j]][j-1] + values[j]
            dp[i][j] = dp[i][j-1]
            if i-weights[j-1] >= 0 and dp[i-weights[j-1]][j-1] + values[j-1] > dp[i][j]:
                dp[i][j] = dp[i-weights[j-1]][j-1] + values[j-1]
    print(dp)

if __name__ == '__main__':
    bag01(weights=[2,2,6,5,4],values=[6,3,5,4,6],capacity=10)