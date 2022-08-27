# leetcode 214, 用kmp算法找回文串，属实巧妙
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def get_next(s):
            length = len(s)
            j,i = -1, 0
            next = [-1] * length
            while i < length-1:
                if j == -1 or s[j] == s[i]:
                    i += 1
                    j += 1
                    next[i] = j
                else:
                    j = next[j]
            return next
        
        def get_palindrome(s):
            s_T = s[::-1]
            length = len(s)
            next = get_next(s)
            i,j=0,0
            while i < length:
                if s[j] == s_T[i] or j == -1:
                    i += 1
                    j += 1
                else:
                    j = next[j]
            if i == length:
                return s[j:][::-1] + s
        
        return get_palindrome(s)
