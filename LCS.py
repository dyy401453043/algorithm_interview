# leetcode 1143, LCS, dp

def Lcs(text1: str, text2: str):
    length1,length2 = len(text1),len(text2)
    dp = [[-float('inf')] * (length2+1) for i in range(length1+1)]
    dp[0][0] = 0
    for len1 in range(length1+1):
        dp[len1][0] = 0
    for len2 in range(length2+1):
        dp[0][len2] = 0
    for len1 in range(1, length1+1):
        for len2 in range(1, length2+1):
            i,j = len1-1, len2-1
            s1,s2 = text1[i],text2[j]
            if s1 == s2:
                dp[len1][len2] = dp[len1-1][len2-1] + 1
            else:
                dp[len1][len2] = max(dp[len1-1][len2], dp[len1][len2-1])
    return dp[len1][len2]

if __name__ == '__main__':
    text1,text2 = "abcde","ace"
    result = Lcs(text1,text2)
    pass