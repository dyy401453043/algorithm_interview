# leetcode299 公牛母牛，数字模拟
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = len([secret[i] for i in range(len(secret)) if secret[i] == guess[i]])
        num_count1,num_count2 = [0]*10,[0]*10
        for i in range(len(secret)):
            num_count1[int(secret[i])] += 1
            num_count2[int(guess[i])] += 1
        num_count = sum([min(num_count1[i],num_count2[i]) for i in range(len(num_count1))])
        return str(bulls) + 'A' + str(num_count-bulls) + 'B'