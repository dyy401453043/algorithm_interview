# leetcode 22，括号生成，dfs+回溯减枝
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(string, left, right):
            if left == n and right == n:
                result.append(string)
                return
            if left < right or left > n or right > n:
                return
            elif left == right:
                dfs(string+'(',left+1,right)
            else:
                dfs(string+'(',left+1,right)
                dfs(string+')',left,right+1)
        dfs('',0,0)
        return result