# leetcode 32 找到最长的有效括号串，两种情况，并列和包含
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0

        result = 0

        dp = [0] * length
        for i in range(length):
            if i == 0:
                continue
            if i == 1:
                dp[i] = 2 if s[0] == '(' and s[1] == ')' else 0
                continue
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                else:
                    dp[i] = dp[i-1] + 2 + dp[i-2-dp[i-1]] if i-1-dp[i-1] >= 0 and s[i-1-dp[i-1]] == '(' else 0
        return max(dp)
