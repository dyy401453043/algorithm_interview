#leetcode 139，检测字符串能否根据词表完美分割，dp，复杂度O(n2)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_word_lenghth = max([len(i) for i in wordDict])
        wordDict = set(wordDict)
        dp = [False] * len(s)
        for i in range(len(s)):
            for j in range(i-max_word_lenghth,i):
                if j < -1:
                    continue
                elif j == -1:
                    dp[i] = dp[i] or (s[j+1:i+1] in wordDict)
                else:
                    dp[i] = dp[i] or (dp[j] and s[j+1:i+1] in wordDict)
        return dp[-1]