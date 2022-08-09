# leetcode 10, 正则表达式匹配, dp
def char_equal(c1, c2):
    return c1 == c2 or c2 == '.'

def match(src, target):
    s, t = len(src), len(target)

    dp = [[False] * (t+1) for i in range(s+1)] # index means length

    dp[0][0] = True

    for j in range(1, len(target)+1):
        dp[0][j] = (target[j-1] == '*' and (dp[0][j-1] or dp[0][j-2]))

    for i in range(1,s+1):
        for j in range(1, t+1):
            dp[i][j] = (char_equal(src[i-1], target[j-1]) and dp[i-1][j-1]) \
            or (target[j-1] == '*' and char_equal(src[i-1], target[j-2]) and dp[i-1][j]) \
            or (target[j-1] == '*' and (dp[i][j-1] or dp[i][j-2]))

    return dp[s][t]

if __name__ == '__main__':
    print("should be true:")
    print(match("", "a*"))
    print(match("", "a*b*"))
    print(match("ab", ".*"))
    print(match("aa", "a*"))

    print("should be false:")
    print(match("", "a"))
    print(match("aa", "a"))
