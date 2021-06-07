# leetcode 5 找最长回文子串
def find_longest_palindrome(string):
    length = len(string)
    dp = [[False] * length for i in range(length)] # 索引为字符串下标
    max_length,sta,end = 0,0,0
    for l in range(1,length+1): # l是真实长度
        for i in range(length):
            j = i + l - 1
            if not j < length:
                continue
            if l == 1:
                dp[i][j] = True
            elif l == 2:
                if string[i] == string[j]:
                    dp[i][j] = True
            else:
                if dp[i+1][j-1] and string[i] == string[j]:
                    dp[i][j] = True
            if dp[i][j] and l > max_length:
                max_length, sta, end = l, i, j
    print(dp)
    return max_length,sta,end


if __name__ == '__main__':
    print(find_longest_palindrome("adabcbaab"))