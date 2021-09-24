# leetcode 60, 找出所有全排列中的第k项，用变治逐步减小规模直接找出第k项，比深度搜索快。
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        # result = []
        # def dfs(permute, candidate):
        #     if len(result) == k:
        #         return
        #     if len(permute) == n:
        #         result.append(permute)
        #     for i in range(len(candidate)):
        #             dfs(permute + [candidate[i]], candidate[:i] + candidate[i+1:])
        # dfs([],[i for i in range(1, n+1)])
        # return ''.join([str(i) for i in result[k-1]])

        factorial = [0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

        def get_first_number_index(k, n, nums):
            if n == 1:
                return 0
            if k % factorial[n-1] == 0:
                index = k // factorial[n-1]-1
            else:
                index = k // factorial[n-1]
            return index
        
        numbers = [i for i in range(1, n+1)]
        result = []
        index = get_first_number_index(k, n, numbers)
        while n > 0:
            index = get_first_number_index(k, n, numbers)
            result.append(numbers[index])
            k = k - index * factorial[n-1]
            numbers = numbers[:index] + numbers[index+1:]
            n = n - 1
        return ''.join([str(i) for i in result])
