# leetcode 316 单调栈解决移除元素后最大的问题
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            ch = s[i]
            if ch in stack: # 不能有相同的，把相同的之间的栈元素移除不会有贡献
                continue
            while len(stack) > 0 and ch < stack[-1]:
                if stack[-1] in s[i+1:]:
                    stack.pop()
                else:
                    break
            stack.append(ch)
        return ''.join(stack)
