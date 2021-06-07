#leetcode 139，检测字符串能否根据词表完美分割，dp，复杂度O(n2),两种方法
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

def check_string_in_vocab(string, vocab):
    length = len(string)
    dp = [False] * length # 索引是下标，0表示第一个字母
    for i in range(length):
        for word in vocab:
            if i-len(word) >= 0:
                if dp[i-len(word)] and string[i-len(word)+1:i+1] == word:
                    dp[i] = True
                    break
            elif i-len(word) == -1:
                if string[i-len(word)+1:i+1] == word:
                    dp[i] = True
                    break
            else:
                pass
    print(dp)
    return dp[-1]

if __name__ == '__main__':
    string = 'two minds is better than one'
    vocab = {' ','s','two','mind','is','better','than','one'}
    print(check_string_in_vocab(string,vocab))