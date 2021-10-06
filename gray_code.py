# leetcode 89，格雷编码的递归性质，比较有意思
import copy
class Solution:
    def grayCode(self, n: int) -> List[int]:
        # dfs 超时 10/16
        # def dfs(string, temp_result):
        #     # nonlocal temp_set
        #     if len(temp_result) == 2 ** n:
        #         return temp_result
        #     hashset = set(temp_result)
        #     for i in range(len(string)):
        #         new_str = string[:i]+ {'0':'1','1':'0'}[string[i]] + string[i+1:]
        #         if new_str not in hashset:
        #             result = dfs(new_str, temp_result+[new_str])
        #             if result:
        #                 return result
        # result = dfs('0'*n, ['0'*n])n
        # return [int(i,2) for i in result]

        # G(n+1) = [0 + G(i, n) for G(i,n) in G(n)] + [1 + G(j, n) for G(j, n) in G(n).reverse()]
        def G(k):
            if k == 1:
                return ['0', '1']
            else:
                Gk = G(k-1)
                return ['0'+ g for g in Gk] + ['1' + g for g in Gk[::-1]]
        return [int(i,2) for i in G(n)]
