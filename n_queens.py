# leetcode 51，N皇后问题，就是全排列dfs和减枝
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        def legal(permute):
            length = len(permute)
            for i in range(length):
                for j in range(i+1,length):
                    distance_row = j - i
                    distance_column = permute[i] - permute[j] if permute[i] > permute[j] else permute[j] - permute[i]
                    if distance_row == distance_column:
                        return False
            return True

        def dfs(permute):
            if not legal(permute):
                return
            if len(permute) == n:
                result.append(permute)
            for i in range(n):
                if i not in permute:
                    dfs(permute + [i])
        
        dfs([])
        result = [['.'*(qn)+'Q'+'.'*(n-qn-1) for qn in permute] for permute in result]
        return result
