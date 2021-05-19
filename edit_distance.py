#leetcode 72 编辑距离 dp。
def minDistance(word1:str, word2:str):
    len1,len2 = len(word1),len(word2)
    dp =[[float('inf')] * (len2+1) for i in range(len1+1)]
    dp[0][0] = 0  #下标表示单词长度
    for length1 in range(len1+1):
        dp[length1][0] = length1
    for length2 in range(len2+1):
        dp[0][length2] = length2
    for length1 in range(1, len1+1):
        for length2 in range(1, len2+1):
            i = length1 - 1
            j = length2 - 1
            # 操作顺序不重要，所以可以只考虑尾部操作
            if word1[i] == word2[j]:
                dp[length1][length2] = dp[length1-1][length2-1]
            else:
                dp[length1][length2] = min(dp[length1-1][length2], dp[length1][length2-1], dp[length1-1][length2-1]) + 1
    return dp[len1][len2]

if __name__ == '__main__':
    word1, word2 = "horse", "ros"
    result = minDistance(word1,word2)
    pass