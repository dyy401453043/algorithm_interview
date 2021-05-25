# leetcode 22，括号生成，dfs+回溯减枝
# 其实这题可以用dp写，比较难想到，"(" + 【i=p时所有括号的排列组合】 + ")" + 【i=q时所有括号的排列组合】
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